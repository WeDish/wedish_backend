from msilib.schema import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .models import Table
from wedish_accounting.models import Order


class TableBooking(LoginRequiredMixin, CreateView):
    model = Table
    fields = ['public_identifier', 'space']
    template_name = 'wedish_pub/table_booking.html'
    success_url = reverse_lazy('wedish_pub:table_booking')


class BarAreaView(LoginRequiredMixin, ListView):
    model = Table
    template_name = 'wedish_pub/bar.html'
    query_set = Table.objects.all()
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class BarTableView(LoginRequiredMixin, DetailView):
    model = Table
    template_name = 'wedish_pub/bar_table.html'
    context_object_name = 'table'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(table=context['table'].id)
        
        return context