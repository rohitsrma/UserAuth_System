# views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class Profile(LoginRequiredMixin, View):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        context = {
            'username': user.username,
            'email': user.email,
            'date': user.date_joined,
            'last_updated':user.last_login 
        }
        return render(request, self.template_name, context)
    
class Dashboard(LoginRequiredMixin, View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        context = {
            'username': user.username,
        }
        return render(request, self.template_name, context)