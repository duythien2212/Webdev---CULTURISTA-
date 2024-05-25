from django.shortcuts import render, get_object_or_404,get_list_or_404
from ..models import Role
from ..serializers import RoleSerializer
from rest_framework import viewsets,status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView
from django.http import JsonResponse

class CreateRole(ListCreateAPIView):
    model = Role
    serializer_class = RoleSerializer

    def get_queryset(self):
        return Role.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Role successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Role unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)
class UpdateRole(RetrieveUpdateDestroyAPIView):
    model = Role
    serializer_class = RoleSerializer

    def get_queryset(self):
        return Role.objects.all()
    
    def put(self, request, *args, **kwargs):
        role_id = request.data.get('role_id')
        roles = get_list_or_404(Role, role_id=role_id)
        for role in roles:
            serializer = RoleSerializer(role ,data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return JsonResponse({
                    'message': 'Update Role unsuccessful!'
                }, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({   
                'message': 'Update Role successful!'
        }, status=status.HTTP_200_OK)

class DeleteRole(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        role_id = request.data.get('role_id') 
        roles = get_list_or_404(Role, role_id=role_id)
        
        for role in roles:
            role.delete()
        
        return JsonResponse({
            'message' : 'Delete Role successfully'
        }, status=status.HTTP_200_OK)
