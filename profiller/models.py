from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profil(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profil')
    bio = models.CharField(max_length=150, null=True, blank=True)
    sehir = models.CharField(max_length=150, null=True, blank=True)
    foto = models.ImageField(null=True, blank=True,
                             upload_to='profile_photos/%Y/%m/')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.foto:
            img = Image.open(self.foto.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.foto.path)


class ProfilMesage(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    message = models.CharField(max_length=240)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profil Mesajı'

    def __str__(self):
        return str(self.profil)
