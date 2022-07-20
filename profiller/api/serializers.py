from dataclasses import fields
from rest_framework import serializers
from profiller.models import Profil, ProfilMesage


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    foto = serializers.ImageField(read_only=True)

    class Meta:
        model = Profil
        fields = '__all__'


class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ['foto']


class ProfilMessageSerializer(serializers.ModelSerializer):
    profil = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfilMesage
        fields = '__all__'
