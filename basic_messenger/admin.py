from django.contrib import admin
from .models import UserProfile, GroupChat, Message


admin.site.register(UserProfile)
admin.site.register(GroupChat)
admin.site.register(Message)
