from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def table_booking(request):
    return render(request, 'wedish_pub/table_booking.html')
