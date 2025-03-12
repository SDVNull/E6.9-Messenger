from rest_framework import serializers
from .models import UserProfile, GroupMessages, PrivateMessages

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'name', 'avatar']

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessages
        fields = ['id', 'name', 'created_time', 'change_time', 'text']

class MPrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateMessages
        fields = ['id', 'sender', 'recipient', 'created_time', 'change_time', 'text']