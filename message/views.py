from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Message
from django.forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MessageSerializer


class Index(TemplateView):
    template_name = 'message/index.html'


class MessageList(ListView):
    model = Message


class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['title', 'text']
    success_url = '../messages'
    exclude = ['user']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MessageCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['title'].widget = TextInput(attrs={'class': 'form-control'})
        form.fields['text'].widget = Textarea(attrs={'class': 'form-control'})
        return form


class ListAPI(APIView):
    def get(self, request, format=None):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
