from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "password", "name"]

    def create(self, validated_data):
        name = validated_data.pop("name")
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        UserProfile.objects.create(user=user, name=name)
        return user


class GroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = "__all__"


class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessages
        fields = "__all__"


class PrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateMessages
        fields = "__all__"
