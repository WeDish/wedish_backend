from django.urls import path
from . import views

app_name = 'wedish_site'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('checkout/', views.CheckoutPageView.as_view(), name='checkout'),  
]
