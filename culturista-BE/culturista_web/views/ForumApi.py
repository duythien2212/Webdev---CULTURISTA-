from django.shortcuts import render, get_object_or_404,get_list_or_404

from ..models import Forum
from ..serializers import ForumSerializer

from rest_framework import viewsets,status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView

from django.http import JsonResponse


class CreateForum(ListCreateAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Forum successful!'
            }, status=status.HTTP_201_CREATED)
        
        return JsonResponse({
            'message': 'Create a new Forum unsuccessful!',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

def searchForum(request, title):
    try:
        forums = Forum.objects.filter(title__icontains=title)
        content_id = [forum.content_id for forum in forums]
        titles = [forum.title for forum in forums]
        tag = [forum.tag for forum in forums]
        replies = [forum.number_of_replies for forum in forums]
        data = {
            'content_id': content_id,
            'titles': titles,
            'tag': tag,
            'replies' : replies
        }
        return JsonResponse(data)
    except Forum.DoesNotExist:
        return JsonResponse({'error': 'None Forum'}, status=404)
