from ast import Not
from rest_framework.generics import GenericAPIView
from profiller.api.serializers import ProfileSerializer, ProfilMessageSerializer, FotoSerializer
from profiller.models import Profil, ProfilMesage
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet
from profiller.api.permissions import KendiProfilYadaReadOnly, DurumMesajıSabibiYadaReadOnly
from rest_framework.filters import SearchFilter


class ProfileViewSet(ListModelMixin, RetrieveModelMixin,  UpdateModelMixin,  GenericViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, KendiProfilYadaReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['sehir']


class ProfilMesajViewSet(ModelViewSet):

    queryset = ProfilMesage.objects.all()
    serializer_class = ProfilMessageSerializer
    permission_classes = [IsAuthenticated, DurumMesajıSabibiYadaReadOnly]

    def get_queryset(self):
        queryset = ProfilMesage.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(profil__user__username=username)
        return queryset

    def perform_create(self, serializer):
        profil = self.request.user.profil
        serializer.save(profil=profil)


class ProfilFotoUpdateView(generics.UpdateAPIView):

    serializer_class = FotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profil_nesnesi = self.request.user.profil
        return profil_nesnesi
