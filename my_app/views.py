from django.shortcuts import render
from .models import testmodels
from .serializers import testserializers
from rest_framework import viewsets
# Create your views here.

class testviews(viewsets.ModelViewSet):
    queryset = testmodels.objects.all()
    serializer_class  = testserializers
