from django.urls import path
from . import views


app_name = 'wedish_pub'
urlpatterns = [
    path('table_booking/', views.TableBooking.as_view(), name='table_booking'),
]
    
    
