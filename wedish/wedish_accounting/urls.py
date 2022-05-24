from django.urls import path
from . import views


app_name = 'wedish_accounting'
urlpatterns = [
    path('bill/', views.BillListView.as_view(), name='bill'),
    path('bill_detail/<int:pk>', views.BillDetailView.as_view(), name='bill_detail'),
    path('bill_summary/<int:pk>', views.bill_summary, name='bill_summary'),
]
