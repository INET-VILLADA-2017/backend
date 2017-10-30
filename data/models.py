# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from simple_history.models import HistoricalRecords


# Create your models here.


class Nursery(models.Model):
    denomination = models.CharField("Denominacion del vivero", max_length=255)
    business_name = models.CharField("Empresa propietaria del establecimiento", max_length=255)
    fiscal_key = models.CharField("Clave fiscal", max_length=16)
    address = models.CharField("Direccion del vivero", max_length=255)
    history = HistoricalRecords()

    def __str__(self):
        return self.business_name


class Param(models.Model):
    name = models.CharField("Nombre del parametro", max_length=255)
    description = models.TextField("Descripcion")

    def __str__(self):
        return self.name


class Sample(models.Model):
    date = models.DateTimeField("Fecha creacion", auto_now_add=True)
    value = models.DecimalField('Valor de la medicion', max_digits=6, decimal_places=4, default=0)
    unit = models.CharField("Unidad de la medicion", max_length=255)
    state_transducer = models.IntegerField("Estado del transductor",
                                           validators=[MinValueValidator(0), MaxValueValidator(2)])
    duration = models.CharField("Duracion", max_length=64)
    state_transmission = models.IntegerField("Estado del transductor",
                                             validators=[MinValueValidator(0), MaxValueValidator(2)])
    nursery = models.ForeignKey(Nursery, on_delete=models.CASCADE, )
    sample = models.ForeignKey(Param, on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return "{value} {unit} {nursery}".format(
            value=self.value,
            unit=self.unit,
            nursery=self.nursery.business_name
        )
