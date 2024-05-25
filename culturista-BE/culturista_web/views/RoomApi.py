from django.shortcuts import render, get_object_or_404,get_list_or_404

from ..models import Room,User
from ..serializers import RoomSerializer

from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView


class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Room successful!'
            }, status=status.HTTP_201_CREATED)
        
        return JsonResponse({
            'message': 'Create a new Room unsuccessful!',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class RoomHandling():
    def join_room(request):
        if request.method == 'GET':
            user_id = request.GET.get('user_id')
            room_id = request.GET.get('room_id')
            try:
                user = User.objects.get(user_id=user_id)
                room = Room.objects.get(room_id=room_id)

                if room.is_full:
                    return JsonResponse({'error': 'Room is full'}, status=400)
                else:
                    user.room=room_id
                    room.number_of_player += 1

                    if room.number_of_player == 4:
                        room.is_full = True

                    room.save()

                    return JsonResponse({'message': 'Joined room successfully'}, status=200)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
            except Room.DoesNotExist:
                return JsonResponse({'error': 'Room not found'}, status=404)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)

    def left_room(request):
        if request.method == 'POST':
            user_id = request.POST.get('user_id')
            room_id = request.POST.get('room_id')
            try:
                user = User.objects.get(user_id=user_id)
                room = Room.objects.get(room_id=room_id)

                user.room=0

                room.number_of_player -= 1

                room.save()

                return JsonResponse({'message': 'User left room successfully'}, status=200)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
            except Room.DoesNotExist:
                return JsonResponse({'error': 'Room not found'}, status=404)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)