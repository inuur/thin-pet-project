from django.urls import path, include
from rest_framework import routers

from .views import TectonicConfinementViewSet, MineralDepositViewSet, WellViewSet

router = routers.DefaultRouter()
router.register(r'tectonic', TectonicConfinementViewSet)
router.register(r'deposit', MineralDepositViewSet)
router.register(r'well', WellViewSet)

urlpatterns = [
    path('', include(router.urls))
]
