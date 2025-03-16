from django.contrib import admin
from .models import UserProfile, GroupMessages, PrivateMessages


admin.site.register(UserProfile)
admin.site.register(GroupMessages)
admin.site.register(PrivateMessages)
