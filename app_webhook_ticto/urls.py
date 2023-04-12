from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("nova-ordem/", views.nova_ordem, name="nova_ordem"),
]