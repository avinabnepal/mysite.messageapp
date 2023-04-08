from django.urls import path
from .views import *


urlpatterns = [
    path('', SignUpView.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', user_logout, name="logout")
]