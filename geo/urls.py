from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'tectonic', TectonicConfinementViewSet)
router.register(r'deposit', MineralDepositViewSet)
router.register(r'well', WellViewSet)
router.register(r'geo-survey', GeophysicalSurveyViewSet)
router.register(r'stratigraphy', StratigraphyViewSet)
router.register(r'sample', SampleViewSet)
router.register(r'thin', ThinViewSet)
router.register(r'thin-section', ThinSectionViewSet)
router.register(r'thin-section-image', ThinSectionImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
