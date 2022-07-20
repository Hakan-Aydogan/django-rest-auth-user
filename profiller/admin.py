from django.contrib import admin
from profiller.models import Profil, ProfilMesage

# Register your models here.


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ('user', 'sehir')


@admin.register(ProfilMesage)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('profil', 'message', 'yaratilma_tarihi')
