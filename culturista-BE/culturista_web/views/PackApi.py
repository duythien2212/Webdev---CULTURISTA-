from django.shortcuts import render, get_object_or_404,get_list_or_404

from ..models import Pack,Question
from ..serializers import PackSerializer

from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView


class CreatePack(ListCreateAPIView):
    model = Pack
    serializer_class = PackSerializer

    def get_queryset(self):
        return Pack.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = PackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Pack successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Pack unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class pack():
    def choosePack(request):
        if request.method == 'GET':
            pack_name = request.GET.get('pack_name')
            try:
                # Kiểm tra xem pack có tồn tại không
                pack = Pack.objects.get(pack_name=pack_name)
                if not pack:
                    return JsonResponse({'error': 'The pack does not exist'}, status=404)
                
                # Lấy danh sách các câu hỏi thuộc pack cụ thể
                questions = Question.objects.filter(pack_name=pack)
                question_content = [question.question_content for question in questions]
                question_answer = [question.answer for question in questions]
                # Trả về các question_id của các câu hỏi
                return JsonResponse({'question_content': question_content,
                                     'question_answer': question_answer})
            
            except Pack.DoesNotExist:
                # Nếu không tìm thấy pack
                return JsonResponse({'error': 'The pack does not exist'}, status=404)
            
            except Exception as e:
                # Xử lý các ngoại lệ khác nếu có
                return JsonResponse({'error': str(e)}, status=500)