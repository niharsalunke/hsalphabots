from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('',views.index),
    re_path(r'^login',views.login),
    re_path(r'^register',views.register),
]