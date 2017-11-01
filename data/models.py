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

    class Meta:
        verbose_name_plural = "Viveros"

    def __str__(self):
        return self.business_name


class Config(models.Model):
    spray_volume = models.DecimalField("Volumen de rociado", max_digits=6, decimal_places=4, default=4)
    degree_of_shadow = models.DecimalField("Grado de sombra", max_digits=6, decimal_places=4, default=8)
    watering_period_1 = models.DecimalField("Periodo de regado uno", max_digits=6, decimal_places=4, default=5)
    watering_period_2 = models.DecimalField("Periodo de regado dos", max_digits=6, decimal_places=4, default=5)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Configuraciones"

    def __str__(self):
        return "{}".format(self.spray_volume)


class Device(models.Model):
    url = models.URLField("Url del dispositivo", default="")
    nursery = models.ForeignKey(Nursery)
    config = models.OneToOneField(Config)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Dispositivos"

    def __str__(self):
        return "{url} {nursery}".format(
            url=self.url,
            nursery=self.nursery.business_name
        )


class Param(models.Model):
    name = models.CharField("Nombre del parametro", max_length=255)
    description = models.TextField("Descripcion")
    color = models.CharField("Color del paramentro", max_length=255)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Parametros"

    def __str__(self):
        return self.name


class Sample(models.Model):
    date = models.DateTimeField("Fecha creacion", auto_now_add=True)
    value = models.DecimalField('Valor de la medicion', max_digits=6, decimal_places=4, default=0)
    unit = models.CharField("Unidad de la medicion", max_length=255)
    state_transducer = models.IntegerField("Estado del transductor",
                                           validators=[MinValueValidator(0), MaxValueValidator(2)])
    duration = models.CharField("Duracion", max_length=64)
    state_transmission = models.IntegerField("Estado de la trasmision",
                                             validators=[MinValueValidator(0), MaxValueValidator(2)])
    nursery = models.ForeignKey(Nursery, on_delete=models.CASCADE, )
    param = models.ForeignKey(Param, on_delete=models.CASCADE)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Registros"

    def __str__(self):
        return "{value} {unit} {nursery}".format(
            value=self.value,
            unit=self.unit,
            nursery=self.nursery.business_name
        )
