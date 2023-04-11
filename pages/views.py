from rest_framework.response import Response
from django.shortcuts import render
from .models import Activity,Book,Video,Data_of_Category,app_Question,Category
from .serializers import HoppiesSerializer,BookSerializer,VideoSerializer,app_QuestionSerializer,data_of_CategorySerializer,CategorySerializer
from rest_framework.decorators import APIView
# from rest_framework import status
# from django.http import JsonResponse
# from django.http import *
# from django import *
from rest_framework import generics
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
   queryset=Category.objects.all()
   serializer_class=CategorySerializer

class ActivitiesViewSet(viewsets.ModelViewSet):
   queryset=Activity.objects.all()
   serializer_class=HoppiesSerializer
class ActivitiesViewSet_pk(viewsets.ModelViewSet):
   queryset=Activity.objects.all()
   serializer_class=HoppiesSerializer
   lookup_field='id'
class BookViewSet(viewsets.ModelViewSet):
   queryset=Book.objects.all()
   serializer_class=BookSerializer
class BookViewSet_pk(viewsets.ModelViewSet):
   queryset=Book.objects.all()
   serializer_class=BookSerializer
   lookup_field='id'
class VideoViewSet(viewsets.ModelViewSet):
   queryset=Video.objects.all()
   serializer_class=VideoSerializer
class VideoViewSet_pk(viewsets.ModelViewSet):
   queryset=Video.objects.all()
   serializer_class=VideoSerializer
   lookup_field='id'
class app_questionViewSet(viewsets.ModelViewSet):
   queryset=app_Question.objects.all()
   serializer_class=app_QuestionSerializer
class app_QuestionViewSet_pk(viewsets.ModelViewSet):
   queryset=app_Question.objects.all()
   serializer_class=app_QuestionSerializer
   lookup_field='id'
class data_of_CategoryViewSet(viewsets.ModelViewSet):
   queryset=Data_of_Category.objects.all()
   serializer_class=data_of_CategorySerializer
class data_of_CategoryViewSet_pk(viewsets.ModelViewSet):
   queryset=Data_of_Category.objects.all()
   serializer_class=data_of_CategorySerializer
   lookup_field='id'

   