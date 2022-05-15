from django.db import models
from django.contrib.auth.models import User
from geo.models import ThinSection, Well

# Create your models here.
from thin.storage.image_storage import ClientDocsStorage


class GranulometricAnalysis(models.Model):
    k_more0_25 = models.FloatField()
    k_01_025 = models.FloatField()
    k_005_01 = models.FloatField()
    k_005_001 = models.FloatField()
    k_less_0_01 = models.FloatField()
    med_dim = models.FloatField()
    k_trusk = models.FloatField()
    st_sort = models.FloatField()
    degree_of_porosity = models.FloatField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    thin_section = models.ForeignKey(
        ThinSection,
        related_name='gran_analyses',
        on_delete=models.CASCADE,
    )


class Report(models.Model):
    well = models.ForeignKey(
        Well,
        on_delete=models.CASCADE,
    )
    granulometric_analysis = models.ForeignKey(
        GranulometricAnalysis,
        on_delete=models.CASCADE,
    )


class ImageAnalyze(models.Model):
    COLOR = "CLR"
    OVERLAY = "OV"
    IMAGE_TYPE = [
        (COLOR, 'color'),
        (OVERLAY, 'overlay'),
    ]
    image = models.FileField(storage=ClientDocsStorage(), null=True, default=None)
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPE, default=None)
    thin_section = models.ForeignKey(
        ThinSection,
        on_delete=models.CASCADE,
    )
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
    )
