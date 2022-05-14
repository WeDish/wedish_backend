from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .models import Table

# Create your views here.

class BarAreaView(LoginRequiredMixin, generic.ListView):
    model = Table
    template_name = 'wedish_pub/bar.html'
    query_set = Table.objects.all()
    login_url = '/login/'
    redirect_field_name = 'redirect_to'