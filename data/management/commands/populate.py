from django.core.management.base import BaseCommand, CommandError
import requests
import json
from data.models import Nursery, Device, Sample, Param


class Command(BaseCommand):
    help = 'Traer los datos de los dispositivos'

    def json_load_byteified(self, file_handle):
        return _byteify(
            json.load(file_handle, object_hook=self._byteify),
            ignore_dicts=True
        )

    def json_loads_byteified(self, json_text):
        return self._byteify(
            json.loads(json_text, object_hook=self._byteify),
            ignore_dicts=True
        )

    def _byteify(self, data, ignore_dicts=False):
        # if this is a unicode string, return its string representation
        if isinstance(data, unicode):
            return data.encode('utf-8')
        # if this is a list of values, return list of byteified values
        if isinstance(data, list):
            return [self._byteify(item, ignore_dicts=True) for item in data]
        # if this is a dictionary, return dictionary of byteified keys and values
        # but only if we haven't already byteified it
        if isinstance(data, dict) and not ignore_dicts:
            return {
                self._byteify(key, ignore_dicts=True): self._byteify(value, ignore_dicts=True)
                for key, value in data.iteritems()
            }
        # if it's anything else, return it in its original form
        return data

    def handle(self, *args, **options):
        devices = Device.objects.all()
        params = {"c": "Temperatura",
                  "%": "Humedad",
                  "z": "Zona de riego",
                  "m3": "Volumen de rociado",
                  "r1": "Producto regado 1",
                  "r2": "Producto regado 2",
                  "so": "Grado de sombra",
                  "s": "Status operativo del vivero",
                  "pr1": "Periodo de regado producto 1",
                  "pr2": "Periodo de regado producto 2"}
        for device in devices:
            # try:
            r = requests.get(device.url)
            data = self.json_loads_byteified(r.content)
            nursery = Nursery.objects.get(fiscal_key=data["v"]["c"])
            for i in data:
                if i != "v":
                    param = Param.objects.get(name__contains=params[i])
                    if i == "%" or i == "c":
                        Sample.objects.create(value=data[i]["v"], unit=i, state_transducer=data[i]["er"],
                                              duration=data[i]["d"], state_transmission=data[i]["en"],
                                              nursery=nursery,
                                              param=param
                                              )
                    else:
                        Sample.objects.create(value=data[i]["v"], unit="placeholder", state_transducer=data[i]["er"],
                                              duration=data[i]["d"], state_transmission=data[i]["en"],
                                              nursery=nursery,
                                              param=param
                                              )
                        # self.stdout.write(self.style.SUCCESS('Successfully'))
                        # except :
                        #   self.stdout.write(self.style.ERROR('ERROR'))
