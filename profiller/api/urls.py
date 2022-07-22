
from django.urls import path, include
import profiller.api.views as as_view
from profiller.api.views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
