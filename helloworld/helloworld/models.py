from django.db import models

class Funcionario(models.Model):

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    lastName = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    serviceTime = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    salary = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

objects = models.Manager()