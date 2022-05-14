from rest_framework import viewsets

from .models import TectonicConfinement, MineralDeposit
from .serializers import TectonicConfinementSerializer, MineralDepositSerializer


class TectonicConfinementViewSet(viewsets.ModelViewSet):
    queryset = TectonicConfinement.objects.all()
    serializer_class = TectonicConfinementSerializer


class MineralDepositViewSet(viewsets.ModelViewSet):
    queryset = MineralDeposit.objects.all()
    serializer_class = MineralDepositSerializer
