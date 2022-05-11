from django.urls import path
from . import views
from .views import (
    ApiGoodListView, ApiGoodDetailView,
)


app_name = 'wedish_menu'
urlpatterns = [
    path('menu/', views.MenuListView.as_view(), name='menu'),
    path('menu_item/<int:pk>', views.MenuItemDetailView.as_view(), name='menu_items_detail'),
    path('api', ApiGoodListView.as_view()),
    path('api/<int:pk>', ApiGoodDetailView.as_view()),
]