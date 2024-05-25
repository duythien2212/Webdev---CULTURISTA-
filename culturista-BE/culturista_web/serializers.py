# myapp/serializers.py
from django.shortcuts import render
from rest_framework import serializers
from .models import Forum,Role,Room,Country,Question,Comment,Assets,User,Pack
from django.contrib.auth import authenticate
from django.http import JsonResponse

import jwt
from django.conf import settings
from django.http import JsonResponse
class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'

class PackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pack
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = User.objects.get(username=username, password=password)
            if user:
                return user
            else:
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ( 'username', 'password','email','age','gender','role','country')
                
    def create(self, validated_data):
        validated_data['is_active'] = True
        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            role=validated_data['role'],
            country=validated_data['country']
        )
        return user
    


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ('content_id','title','content','tag','user_created_name')
    def create(self,validated_data):
        forum = Forum.objects.create(
            content_id = validated_data['content_id'],
            title = validated_data['title'],
            content = validated_data['content'],
            tag = validated_data['tag'],
            user_created_name = validated_data['user_created_name']
        )
        return forum

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_id','user_name','comment_content','content_id')
    def create(self, validated_data):
        #
    
        # Create a comment with the provided data
        comment = Comment.objects.create(
            comment_id=validated_data['comment_id'],
            user_name=validated_data['user_name'],
            comment_content=validated_data['comment_content'],
            content_id=validated_data['content_id']
        )
        content_id = (validated_data.get('content_id')).content_id
        
        # Fetch the related Forum object
        forum = Forum.objects.get(content_id=content_id)
        # Increment the number_of_replies and save the Forum object
        if forum :
            forum.number_of_replies += 1
            forum.save()
        else :
            raise serializers.ValidationError("forum is not exits")
        return comment
