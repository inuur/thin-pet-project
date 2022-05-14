from rest_framework import viewsets

from .serializers import *
from .models import *


class GranulometricAnalysisViewSet(viewsets.ModelViewSet):
    queryset = GranulometricAnalysis.objects.all()
    serializer_class = GranulometricAnalysisSerializer
