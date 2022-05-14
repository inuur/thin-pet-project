from rest_framework import serializers

from .models import (
    TectonicConfinement,
    MineralDeposit,
    Well,
)


class WellSerializer(serializers.ModelSerializer):
    show = serializers.SerializerMethodField('get_show')
    link = serializers.SerializerMethodField('get_link')

    @staticmethod
    def get_show(obj):
        return False

    @staticmethod
    def get_link(obj):
        return f'/well/{obj.id}'

    class Meta:
        model = Well
        fields = '__all__'


class MineralDepositSerializer(serializers.ModelSerializer):
    wells = WellSerializer(many=True, read_only=True)
    show = serializers.SerializerMethodField('get_show')
    link = serializers.SerializerMethodField('get_link')

    @staticmethod
    def get_show(obj):
        return False

    @staticmethod
    def get_link(obj):
        return f'/deposit/{obj.id}'

    class Meta:
        model = MineralDeposit
        fields = '__all__'


class TectonicConfinementSerializer(serializers.ModelSerializer):
    mineral_deposits = MineralDepositSerializer(many=True, read_only=True)
    show = serializers.SerializerMethodField('get_show')
    link = serializers.SerializerMethodField('get_link')

    @staticmethod
    def get_show(obj):
        return False

    @staticmethod
    def get_link(obj):
        return f'/tectonic/{obj.id}'

    class Meta:
        model = TectonicConfinement
        fields = '__all__'
