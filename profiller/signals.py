from django.db.models.signals import post_save
from django.dispatch import receiver
from profiller.models import Profil, ProfilMesage
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_profil(sender, instance, created, **kwargs):

    if created:
        Profil.objects.create(user=instance)


@receiver(post_save, sender=Profil)
def create_profil_message(sender, instance, created, **kwargs):

    if created:
        ProfilMesage.objects.create(
            profil=instance, message=f'{instance.user.username} Klube Katıldı')
