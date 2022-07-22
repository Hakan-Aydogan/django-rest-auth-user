
from django.urls import path, include
import profiller.api.views as as_view
from profiller.api.views import ProfileViewSet, ProfilMesajViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'durum', ProfilMesajViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
