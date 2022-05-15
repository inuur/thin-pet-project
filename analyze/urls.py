from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'gran-analyse', GranulometricAnalysisViewSet)
router.register(r'analyze', FullAnalysisViewSet, basename='analyze')
router.register(r'analyze', ColorAnalysisViewSet, basename='analyze')
router.register(r'analyze', OverlayAnalysisViewSet, basename='analyze')

urlpatterns = [
    path('', include(router.urls))
]
