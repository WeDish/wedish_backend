from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, FormMixin

from .forms import UserRegisterForm, UserUpdateForm


def index(request):
    return render(request, 'wedish_site/index.html')


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'wedish_site/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = _('Your profile was created successfully')


class UserProfileView(LoginRequiredMixin, DetailView, FormMixin):
    model = User
    template_name = 'wedish_site/profile.html'
    form_class = UserUpdateForm
    
    def get_success_url(self):
        return reverse_lazy('wedish_site:profile', kwargs={'pk' : self.object.id})

    def get_context_data(self, *args, **kwargs):
        context= super(UserProfileView, self).get_context_data(**kwargs)
        context['form'] = UserUpdateForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Profile updated successfuly.'))
            return redirect(reverse_lazy('wedish_site:profile'))
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render (request, 'wedish_site/profile.html', context=context)
    