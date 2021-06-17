from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .models import Foo, Bar, Ent, Det
from .forms import MyForm
from django.utils import timezone
from django.template.loader import render_to_string
import json

class IndexView(generic.View):
    template_name = 'myapp/index.html'
    context_object_name = 'dummy'
    def setup(self, request, *args, **kwargs):
        return super(IndexView, self).setup(request, *args, **kwargs)
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return HttpResponse("success post in your generic.View class!")

class TpltView(generic.TemplateView):
    template_name = 'myapp/tpltview.html'
    context_object_name = "myctx"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foo'] = "bar"
        return context

class MyFormView(generic.FormView):
    template_name = 'myapp/formtplt.html'
    form_class = MyForm
    success_url = reverse_lazy('myapp:index')
    success_url = '/myapp/list_view'

    def form_valid(self, form):
        """ called after form data POSTed"""
        form.do_stuff()
        return super(MyFormView, self).form_valid(form)
    
    def form_invalid(self, form):
        super(MyFormView, self).form_invalid(form)

class BasicDetailedView(generic.DetailView):
    template_name = 'myapp/basic_detailed_view.html'
    context_object_name = 'my_ctx'
    model = Bar

    def get_context_data(self, **kwargs):
        """ overriding the get_context_data() so add additional stuff to it."""
        context = super().get_context_data(**kwargs)
        context['added_vars'] = {'v1':1, 'v2':2}
        return context

    def get(self, request, *args, **kwargs):
        """ overriding the detailed view get() method. """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class BasicListView(generic.ListView):
    template_name = 'myapp/list_view.html'
    context_object_name = 'foo_list'
    model = Foo

    def get_context_data(self, **kwargs):
        """ overriding the get_context_data() so add additional stuff to it."""
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['fields'] = Foo._meta.get_fields()
        return context


class AjaxView(generic.ListView):
    template_name = 'myapp/ajax_list.html'
    context_object_name = 'foo_list'
    model = Ent


class AjaxDetails(generic.View):
    """ this view used just to send the data needed for the ajax functions
    to populate the details section div
    """
    def get(self, request, *args, **kwargs):
        pk = int(request.GET["pk"])
        objs = Ent.objects.get(pk=pk).dets.all()
        # this renders the template into fully-formed html
        details = render_to_string('myapp/details.html', {"object_list":objs})
        # we still need to wrapped that html string into an HTTP response
        return HttpResponse(details)