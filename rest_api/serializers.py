from rest_framework import serializers

from .models import (
    TectonicConfinement,
    MineralDeposit,
    Well,
)


class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = '__all__'


class MineralDepositSerializer(serializers.ModelSerializer):
    wells = WellSerializer(many=True, read_only=True)

    class Meta:
        model = MineralDeposit
        fields = '__all__'


class TectonicConfinementSerializer(serializers.ModelSerializer):
    mineral_deposits = MineralDepositSerializer(many=True, read_only=True)

    class Meta:
        model = TectonicConfinement
        fields = '__all__'
