from django.shortcuts import render
from rest_framework import viewsets
from .models import Messages
from .serializers import MessagesSerializer

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
