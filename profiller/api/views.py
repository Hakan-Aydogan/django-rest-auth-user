from rest_framework.generics import GenericAPIView
from profiller.api.serializers import ProfileSerializer, ProfilMessageSerializer, FotoSerializer
from profiller.models import Profil, ProfilMesage
from rest_framework import generics


class ProfilListCreateAPIView(generics.ListAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfileSerializer
