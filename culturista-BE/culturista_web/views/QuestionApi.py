from django.shortcuts import render, get_object_or_404,get_list_or_404

from ..models import Question
from ..serializers import QuestionSerializer
from django.http import JsonResponse

from rest_framework import viewsets,status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView

from django.http import JsonResponse

class CreateQuestion(ListCreateAPIView):
    model = Question
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Question successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Question unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)
class UpdateQuestion(RetrieveUpdateDestroyAPIView):
    model = Question
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()
    
    def put(self, request, *args, **kwargs):
        question_id = request.data.get('question_id')
        questions = get_list_or_404(Question, question_id=question_id)
        for question in questions:
            serializer = QuestionSerializer(question ,data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return JsonResponse({
                    'message': 'Update Question unsuccessful!'
                }, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({   
                'message': 'Update Question successful!'
        }, status=status.HTTP_200_OK)

class DeleteQuestion(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        question_id = request.data.get('question_id') 
        questions = get_list_or_404(Question, question_id=question_id)
        
        for question in questions:
            question.delete()
        
        return JsonResponse({
            'message' : 'Delete Question successfully'
        }, status=status.HTTP_200_OK)


def get_question_detail(request, question_id):
    try:
        question = Question.objects.get(question_id=question_id)
        data = {
            'question_content': question.question_content,
            'answer': question.answer,
        }
        return JsonResponse(data)
    except Question.DoesNotExist:
        return JsonResponse({'error': 'Question not found'}, status=404)
