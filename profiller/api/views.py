from rest_framework.generics import GenericAPIView
from profiller.api.serializers import ProfileSerializer, ProfilMessageSerializer, FotoSerializer
from profiller.models import Profil, ProfilMesage
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet
from profiller.api.permissions import KendiProfilYadaReadOnly, DurumMesajıSabibiYadaReadOnly


class ProfileViewSet(ListModelMixin, RetrieveModelMixin,  UpdateModelMixin,  GenericViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, KendiProfilYadaReadOnly]


class ProfilMesajViewSet(ModelViewSet):

    queryset = ProfilMesage.objects.all()
    serializer_class = ProfilMessageSerializer
    permission_classes = [IsAuthenticated, DurumMesajıSabibiYadaReadOnly]

    def perform_create(self, serializer):
        profil = self.request.user.profil
        serializer.save(profil=profil)
