from rest_framework import serializers

from .models import TectonicConfinement, MineralDeposit


class MineralDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = MineralDeposit
        fields = '__all__'


class TectonicConfinementSerializer(serializers.ModelSerializer):
    mineral_deposits = MineralDepositSerializer(many=True)

    class Meta:
        model = TectonicConfinement
        fields = '__all__'
