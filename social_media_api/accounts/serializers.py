from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from posts.models import Post

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password', None)
        user = get_user_model().objects.create_user(**validated_data, password=password)
        Token.objects.create(user=user)
        return user


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # Explicit
    email = serializers.CharField()     # Explicit
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password', None)
        user = get_user_model().objects.create_user(**validated_data, password=password)
        Token.objects.create(user=user)
        return user

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'followers_count', 'following_count']

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()


class FollowUnfollowSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def validate_user_id(self, value):
        try:
            User.objects.get(id=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")
        return value
    
class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at']    