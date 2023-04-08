from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, View
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import logout


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return self.redirect_to_success_url()
        return super().dispatch(request, *args, **kwargs)
        
    def redirect_to_success_url(self):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return 'login'


class Login(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return '/app/'

    def get_redirect_url(self):
        return '/app/'

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')