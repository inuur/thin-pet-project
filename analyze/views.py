from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *
from .service.analyze import color_analyze, cover_analyze


class GranulometricAnalysisViewSet(viewsets.ModelViewSet):
    queryset = GranulometricAnalysis.objects.all()
    serializer_class = GranulometricAnalysisSerializer


class FullAnalysisViewSet(viewsets.ViewSet):
    @action(methods=['POST'], detail=True, url_path='')
    def full(self, request, pk=None):
        pass


class ColorAnalysisViewSet(viewsets.ViewSet):
    @action(methods=['POST'], detail=True, url_path='')
    def color(self, request, pk=None):
        image_analyze = color_analyze(pk)
        return Response({'image_analyze': image_analyze})


class CoverAnalysisViewSet(viewsets.ViewSet):
    @action(methods=['POST'], detail=True, url_path='')
    def cover(self, request, pk=None):
        image_analyze = cover_analyze(pk)
        return Response({'image_analyze': image_analyze})
