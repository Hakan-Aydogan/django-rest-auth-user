from rest_framework.generics import GenericAPIView
from profiller.api.serializers import ProfileSerializer, ProfilMessageSerializer, FotoSerializer
from profiller.models import Profil, ProfilMesage
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from profiller.api.permissions import KendiProfilYadaReadOnly


class ProfileViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, KendiProfilYadaReadOnly]
