from rest_framework import viewsets

from .serializers import *
from .models import *


class TectonicConfinementViewSet(viewsets.ModelViewSet):
    queryset = TectonicConfinement.objects.all()
    serializer_class = TectonicConfinementSerializer


class MineralDepositViewSet(viewsets.ModelViewSet):
    queryset = MineralDeposit.objects.all()
    serializer_class = MineralDepositSerializer


class WellViewSet(viewsets.ModelViewSet):
    queryset = Well.objects.all()
    serializer_class = WellSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class ThinViewSet(viewsets.ModelViewSet):
    queryset = Thin.objects.all()
    serializer_class = ThinSerializer


class ThinSectionViewSet(viewsets.ModelViewSet):
    queryset = ThinSection.objects.all()
    serializer_class = ThinSectionSerializer
