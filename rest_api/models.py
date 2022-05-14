from django.db import models


class TectonicConfinement(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MineralDeposit(models.Model):
    name = models.CharField(max_length=255)
    tectonic_confinement = models.ForeignKey(
        TectonicConfinement,
        related_name='mineral_deposits',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Well(models.Model):
    name = models.CharField(max_length=50)
    mineral_deposit = models.ForeignKey(
        MineralDeposit,
        related_name='wells',
        on_delete=models.CASCADE,
    )
    depth = models.CharField(max_length=70)

    def __str__(self):
        return self.name
