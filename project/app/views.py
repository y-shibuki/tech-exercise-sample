from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic


# TODO: Viewの作成
class SampleTemplateView(generic.TemplateView):
    template_name = "app/index.html"