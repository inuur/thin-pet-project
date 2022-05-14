from rest_framework import serializers

from .models import TectonicConfinement, MineralDeposit


class TectonicConfinementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TectonicConfinement
        fields = '__all__'


class MineralDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = MineralDeposit
        fields = '__all__'
