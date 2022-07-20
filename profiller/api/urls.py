
from django.urls import path
import profiller.api.views as as_view


urlpatterns = [
    path('profil/', as_view.ProfilListCreateAPIView.as_view(), name='profil'),
]
