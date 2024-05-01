from django.shortcuts import render

from .models import Reaction
from .serializers import ReactionSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class ReactionsList(APIView):
    def get(self, request, format = None):
        reactions = Reaction.objects.all().order_by('name')
        serializer = ReactionSerializer(reactions, many= True)
        return Response(serializer.data)
