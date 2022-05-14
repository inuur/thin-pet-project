from rest_framework import serializers

from .models import *


class GranulometricAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = GranulometricAnalysis
        fields = '__all__'
