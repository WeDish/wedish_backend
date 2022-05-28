from django.urls import path
from . import views


app_name = 'wedish_pub'
urlpatterns = [
    path('table_booking/', views.TableBooking.as_view(), name='table_booking'),
    path('bar/', views.BarAreaView.as_view(), name='bar'),
    path('table/<int:pk>/', views.BarTableView.as_view(), name='bar_table'),
]
    
    
