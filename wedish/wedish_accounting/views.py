from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions
from .models import Bill, Company, Order
from django.core.paginator import Paginator
from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML, CSS
import datetime

from django.template.loader import render_to_string
import tempfile
from django.db.models import Sum
from io import BytesIO
import weasyprint

class BillListView(generic.ListView):
    model = Bill
    template_name = 'wedish_accounting/bill.html'
    context_object_name = 'bills'
    queryset = Bill.objects.all()
    paginate_by = 2


class BillDetailView(generic.DetailView):
    model = Bill
    template_name = 'wedish_accounting/bill_detail.html'
    context_object_name = 'bill_detail'

def render_pdf_view(template, context, request):
    context.update({
        'request': request,
    })

    pdf = weasyprint.HTML(string=str(template.render(context)))
    pdf_file = BytesIO()
    pdf_file.write(pdf.write_pdf())
    pdf_file.seek(0)
    return HttpResponse(pdf_file, content_type='application/pdf')

def bill_summary(request, pk):
    template = get_template('wedish_accounting/bill_detail.html')
    bill_detail = Bill.objects.get(pk=pk)
    context = {
        'bill_detail': bill_detail,
    }
    return render_pdf_view(template, context, request)





