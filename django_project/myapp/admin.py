from django.contrib import admin
from .models import Bar, Foo, MyUser
# Register your models here.

admin.site.register(Foo)
admin.site.register(Bar)
admin.site.register(MyUser)