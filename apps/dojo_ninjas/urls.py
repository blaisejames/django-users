from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'dojo_ninjas/$', views.index)
]