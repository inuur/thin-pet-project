from rest_framework import serializers

from .models import (
    TectonicConfinement,
    MineralDeposit,
    Well,
)


class WellSerializer(serializers.ModelSerializer):
    show = serializers.BooleanField(default=False, read_only=True)
    link = serializers.SerializerMethodField('get_link', read_only=True)

    @staticmethod
    def get_link(obj):
        return f'/well/{obj.id}'

    class Meta:
        model = Well
        fields = '__all__'


class MineralDepositSerializer(serializers.ModelSerializer):
    wells = WellSerializer(many=True, read_only=True)
    show = serializers.BooleanField(default=False, read_only=True)
    link = serializers.SerializerMethodField('get_link', read_only=True)

    @staticmethod
    def get_link(obj):
        return f'/deposit/{obj.id}'

    class Meta:
        model = MineralDeposit
        fields = '__all__'


class TectonicConfinementSerializer(serializers.ModelSerializer):
    mineral_deposits = MineralDepositSerializer(many=True, read_only=True)
    show = serializers.BooleanField(default=False, read_only=True)
    link = serializers.SerializerMethodField('get_link', read_only=True)

    @staticmethod
    def get_link(obj):
        return f'/tectonic/{obj.id}'

    class Meta:
        model = TectonicConfinement
        fields = '__all__'
