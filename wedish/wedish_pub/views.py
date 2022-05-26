from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Table


class TableBooking(LoginRequiredMixin, CreateView):
    model = Table
    fields = ['public_identifier', 'space']
    template_name = 'wedish_pub/table_booking.html'
    success_url = reverse_lazy('wedish_pub:table_booking')
