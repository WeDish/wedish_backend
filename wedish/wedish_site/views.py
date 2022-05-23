from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView

from .forms import UserRegisterForm


def index(request):
    return render(request, 'wedish_site/index.html')


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'wedish_site/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = _('Your profile was created successfully')
