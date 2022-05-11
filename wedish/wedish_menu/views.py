from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .models import Menu, MenuItem, Category
from .serializers import GoodSerializer
from rest_framework import generics, permissions
from .models import Good


class MenuListView(generic.ListView):
    model = MenuItem
    template_name = 'wedish_menu/menu.html'
    context_object_name = 'menu_items'
    queryset = MenuItem.objects.all()
    paginate_by = 4


class MenuItemDetailView(generic.DetailView):
    model = MenuItem
    template_name = 'wedish_menu/menu_item.html'
    context_object_name = 'menu_items_detail'

    # def get_success_url(self):
    #     return reverse_lazy('wedish_menu:menu_items_detail', kwargs={'pk': self.object.id})


class ApiGoodListView(generics.ListCreateAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ApiGoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
