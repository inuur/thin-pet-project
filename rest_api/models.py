from django.db import models


class TectonicConfinement(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.name


class MineralDeposit(models.Model):
    name = models.CharField(
        max_length=255
    )
    tectonic_confinement = models.ForeignKey(
        TectonicConfinement,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
