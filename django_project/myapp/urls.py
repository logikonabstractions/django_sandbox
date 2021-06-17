# asdf
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('basic_detailed_view/<int:pk>/', views.BasicDetailedView.as_view(), name='basicdetailed'),
    path('list_view/', views.BasicListView.as_view(), name='listview'),
    path('tpltview/', views.TpltView.as_view(), name='tpltview'),
    path('formview/', views.MyFormView.as_view(), name='formview'),
    path('ajax_listview/', views.AjaxView.as_view(), name='ajaxview'),
    path('get_ajax_details/', views.AjaxDetails.as_view(), name='ajaxdetails'),
]
