from django.shortcuts import render, get_object_or_404,get_list_or_404

from ..models import Country
from ..serializers import CountrySerializer

from rest_framework import viewsets,status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView

from django.http import JsonResponse

class CreateCountry(ListCreateAPIView):
    model = Country
    serializer_class = CountrySerializer

    def get_queryset(self):
        return Country.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Country  successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Country  unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)
class UpdateCountry(RetrieveUpdateDestroyAPIView):
    model = Country
    serializer_class = CountrySerializer

    def get_queryset(self):
        return Country.objects.all()
    
    def put(self, request, *args, **kwargs):
        country_id = request.data.get('country_code')
        countries = get_list_or_404(Country, country_id=country_id)
        for country in countries:
            serializer = CountrySerializer(country ,data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return JsonResponse({
                    'message': 'Update Country unsuccessful!'
                }, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({   
                'message': 'Update Country successful!'
        }, status=status.HTTP_200_OK)

class DeleteCountry(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        country_code = request.data.get('country_code') 
        countries= get_list_or_404(Country, country_code = country_code )
        
        for country in countries:
            country.delete()
        
        return JsonResponse({
            'message' : 'Delete Country successfully'
        }, status=status.HTTP_200_OK)
