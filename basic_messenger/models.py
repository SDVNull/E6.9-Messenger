from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)


class GroupChat(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="group_chats")
    created_time = models.DateTimeField(auto_now_add=True)


class GroupMessages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    change_time = models.DateTimeField(null=True, blank=True)
    text = models.TextField()
    group = models.ForeignKey(GroupChat, on_delete=models.CASCADE)


class PrivateMessages(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name="recipient", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    change_time = models.DateTimeField(null=True, blank=True)
    text = models.TextField()
