from django.shortcuts import render, get_object_or_404,get_list_or_404

from ..models import Comment
from ..serializers import CommentSerializer

from rest_framework import viewsets,status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView

from django.http import JsonResponse


class CreateComment(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new comment successful!'
            }, status=status.HTTP_201_CREATED)
        
        return JsonResponse({
            'message': 'Create a new comment unsuccessful!',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

