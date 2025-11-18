from django.contrib import admin
from .models import Cliente, Empleado, Servicio, ContratoServicio

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Servicio)
admin.site.register(ContratoServicio)