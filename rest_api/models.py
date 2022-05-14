from django.db import models

from thin.storage.image_storage import ClientDocsStorage


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
    depth = models.CharField(max_length=70)
    photo_kern = models.FileField(
        storage=ClientDocsStorage(),
        blank=True,
        default=None
    )
    mineral_deposit = models.ForeignKey(
        MineralDeposit,
        related_name='wells',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Sample(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(
        storage=ClientDocsStorage(),
        blank=True,
        default=None
    )
    well = models.ForeignKey(
        Well,
        related_name='samples',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Thin(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(
        storage=ClientDocsStorage(),
        blank=True,
        default=None
    )
    sample = models.ForeignKey(
        Sample,
        related_name='thins',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class ThinSection(models.Model):
    name = models.CharField(max_length=50)
    thin = models.ForeignKey(
        Thin,
        related_name='thin_sections',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
