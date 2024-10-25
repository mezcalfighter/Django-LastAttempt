from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello_world/",views.hello_world,name="hello_world"),
    path("",views.index,name="index"),
]
