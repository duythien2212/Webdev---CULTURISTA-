# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from googletrans import Translator
from googletrans.exceptions import TranslateException

class TranslateMessage(APIView):
    def post(self, request):
        message = request.data.get('message', '')
        target_language = request.data.get('target_language', 'en')  # Default target language is English

        try:
            # Translate the message
            translator = Translator()
            translated_message = translator.translate(message, dest=target_language)
            
            return Response({'translated_message': translated_message.text})
        except TranslateException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)