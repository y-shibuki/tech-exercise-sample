from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.SampleTemplateView.as_view(), name="index"),
]