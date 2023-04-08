from django.contrib import admin
from .models import Message

model_list = [Message]
admin.site.register(model_list)
