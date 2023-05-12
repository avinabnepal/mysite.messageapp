from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('messages/', views.MessageList.as_view(), name="messages"),
    path('create/', login_required(views.MessageCreate.as_view()), name="create"),
    path('api/', views.ListAPI.as_view(), name="api"),
]