from rest_framework import viewsets

from .models import (
    TectonicConfinement,
    MineralDeposit,
    Well,
)
from .serializers import (
    TectonicConfinementSerializer,
    MineralDepositSerializer,
    WellSerializer,
)


class TectonicConfinementViewSet(viewsets.ModelViewSet):
    queryset = TectonicConfinement.objects.all()
    serializer_class = TectonicConfinementSerializer


class MineralDepositViewSet(viewsets.ModelViewSet):
    queryset = MineralDeposit.objects.all()
    serializer_class = MineralDepositSerializer


class WellViewSet(viewsets.ModelViewSet):
    queryset = Well.objects.all()
    serializer_class = WellSerializer
