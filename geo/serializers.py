from rest_framework import serializers

from .models import *


class ThinSectionImageSerializer(serializers.ModelSerializer):
    show = serializers.BooleanField(default=False, read_only=True)
    link = serializers.SerializerMethodField('get_link', read_only=True)

    @staticmethod
    def get_link(obj):
        return f'/thin-section-image/{obj.id}'

    class Meta:
        model = ThinSectionImage
        fields = '__all__'


class ThinSectionSerializer(serializers.ModelSerializer):
    images = ThinSectionImageSerializer(many=True, read_only=True)
    show = serializers.BooleanField(default=False, read_only=True)
    link = serializers.SerializerMethodField('get_link', read_only=True)

    @staticmethod
    def get_link(obj):
        return f'/thin-section/{obj.id}'

    class Meta:
        model = ThinSection
        fields = '__all__'


class ThinSerializer(serializers.ModelSerializer):
    thin_sections = ThinSectionSerializer(many=True, read_only=True)
    show = serializers.BooleanField(default=False, read_only=True)
    link = serializers.SerializerMethodField('get_link', read_only=True)

    @staticmethod
    def get_link(obj):
        return f'/thin/{obj.id}'

    class Meta:
        model = Thin
        fields = '__all__'


class SampleSerializer(serializers.ModelSerializer):
    thins = ThinSerializer(many=True, read_only=True)
    show = serializers.BooleanField(default=False, read_only=True)
    link = serializers.SerializerMethodField('get_link', read_only=True)

    @staticmethod
    def get_link(obj):
        return f'/sample/{obj.id}'

    class Meta:
        model = Sample
        fields = '__all__'


class StratigraphySerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField('get_link', read_only=True)

    @staticmethod
    def get_link(obj):
        return f'/stratigraphy/{obj.id}'

    class Meta:
        model = Stratigraphy
        fields = '__all__'


class GeophysicalSurveySerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField('get_link', read_only=True)

    @staticmethod
    def get_link(obj):
        return f'/geo-survey/{obj.id}'

    class Meta:
        model = GeophysicalSurvey
        fields = '__all__'


class WellSerializer(serializers.ModelSerializer):
    geo_surveys = GeophysicalSurveySerializer(many=True, read_only=True)
    stratigraphies = StratigraphySerializer(many=True, read_only=True)
    samples = SampleSerializer(many=True, read_only=True)
    show = serializers.BooleanField(default=False, read_only=True)
    show_sample = serializers.BooleanField(default=False, read_only=True)
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
