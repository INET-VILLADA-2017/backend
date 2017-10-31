from django.core.management.base import BaseCommand, CommandError
from data.models import Param


class Command(BaseCommand):
    help = 'Cargar todos los parametros necesarios para el funcionamiento de la aplicacion'

    def handle(self, *args, **options):
        colors = ["#F44436", "#03A9F4", "#8BC34A", "#E91E63", "#9C2790", "#673AB7", "#3F51B5", "#2196F3", "#009688",
                  "#FF9866"]
        params = ["Temperatura", "Humedad", "Zona de riego", "Volumen de rociado", "Producto regado 1",
                  "Producto regado 2", "Grado de sombra", "Status operativo del vivero", "Periodo de regado producto 1",
                  "Periodo de regado producto 2"]
        for param, color in zip(params, colors):
            try:
                description = "Este es el parametro {p}".format(p=param)
                Param.objects.create(name=param, description=description, color=color)
            except:
                self.stdout.write(self.style.ERROR('Error'))

        self.stdout.write(self.style.SUCCESS('Successfully'))
