from django.urls import path
from . import views

app_name = 'wedish_pub'
urlpatterns = [
    path('pub/', views.MenuListView.as_view(), name='menu'),

]