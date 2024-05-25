from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from rest_framework.response import Response
from ..models import Forum

def index_page(request):
    return render(request, 'index.html')

def login_user(request):
    return render(request, 'pages/login.html')

def register_user(request):
    return render(request, 'pages/register.html')

def find_forum(request):
    return render(request, 'pages/findforum.html')

def chat_page(request):
    return render(request, 'pages/chat.html')

def play(request, roomID):
    return render(request, 'pages/play.html', {"roomID" : roomID})

def find_room(request):
    return render(request, 'pages/findRoom.html')

def create_forum(request):
    return render(request, 'pages/formForum.html')

def forum(request, content_id):
    try:
        forum = Forum.objects.get(pk=content_id)
        data = {
            "content_id" : forum.content_id,
            "title" : forum.title,
            "content" : forum.content,
            "tag" : forum.tag,
            "replies" : forum.number_of_replies,
        }
        return render(request, 'pages/forum.html', data)
    except Forum.DoesNotExist:
        return redirect('index')

def profile(request):
    return render(request, 'pages/profile.html')