from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GametrackerSerializer
from .models import Gametracker
# Create your views here.

class GametrackerView(viewsets.ModelViewSet):
    serializer_class = GametrackerSerializer
    queryset = Gametracker.objects.all()
