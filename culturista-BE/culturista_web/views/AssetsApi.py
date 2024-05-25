from django.shortcuts import render, get_object_or_404,get_list_or_404

from ..models import Assets
from ..serializers import AssetsSerializer

from rest_framework import viewsets,status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView

from django.http import JsonResponse

