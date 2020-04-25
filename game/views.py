from django.shortcuts import render
from .models import Players
from .serializers import PlayersSerializer
from rest_framework import viewsets

class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
