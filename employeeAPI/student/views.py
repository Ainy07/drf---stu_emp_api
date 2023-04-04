from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from . serializer import *
from .models import *
# Create your views here.
class StudentCreateApi(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentUpdateApi(generics.RetrieveUpdateAPIView) :
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentDeleteApi(generics.DestroyAPIView) :
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentApi(generics.ListAPIView) :
    queryset = Student.objects.all()
    serializer_class = StudentSerializer         