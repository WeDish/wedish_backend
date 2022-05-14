from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from .models import Table
from wedish_accounting.models import Order

# Create your views here.

class BarAreaView(LoginRequiredMixin, generic.ListView):
    model = Table
    template_name = 'wedish_pub/bar.html'
    query_set = Table.objects.all()
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class BarTableView(LoginRequiredMixin, generic.DetailView):
    model= Order
    template_name= 'wedish_pub/bar_table.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['order'] = Order.objects.all()
        return context

