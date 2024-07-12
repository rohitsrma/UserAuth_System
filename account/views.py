# views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin

"""To create this project i have used Django's built-in authentication views along with some custom views. 
    The URL configuration maps various routes to these views, including login, logout, password reset, and password change, utilizing Django's built-in functionalities.
    Custom views handle user registration (SignUpView), profile display (Profile), and a simple user dashboard (Dashboard). 
    The SignUpView uses a custom form (SignUpForm) to manage user registrations and redirects users to the login page upon successful registration. 
    The Profile view, accessible only to logged-in users, displays detailed user information such as username, email, join date, and last login time. 
    Similarly, the Dashboard view shows the logged-in user's username. Both Profile and Dashboard views uses the LoginRequiredMixin to ensure that only authenticated users can access these pages, redirecting unauthenticated users to the login page."""

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