from django.db import models
from django.contrib.auth.models import User
from geo.models import ThinSection


# Create your models here.
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
