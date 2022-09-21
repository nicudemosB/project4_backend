from django.shortcuts import render
from rest_framework import generics
from .serializers import CharacterSerializer
from .models import Character
# Create your views here.
class CharacterList(generics.ListCreateAPIView):
    queryset = Character.objects.all().order_by('id')
    serializer_class = CharacterSerializer

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all().order_by('id')
    serializer_class = CharacterSerializer