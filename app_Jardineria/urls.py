from django.urls import path
from . import views

urlpatterns = [
    # URLs Generales
    path('', views.inicio_jardineria, name='inicio_jardineria'),

    # URLs Cliente
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/actualizar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),

    # URLs Empleado
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/<int:empleado_id>/', views.detalle_empleado, name='detalle_empleado'),
    path('empleados/actualizar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),

    # URLs Servicio
    path('servicios/', views.ver_servicios, name='ver_servicios'),
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/<int:servicio_id>/', views.detalle_servicio, name='detalle_servicio'),
    path('servicios/actualizar/<int:servicio_id>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('servicios/borrar/<int:servicio_id>/', views.borrar_servicio, name='borrar_servicio'),

    # URLs ContratoServicio (para ver las relaciones)
    path('contratos/', views.ver_contratos, name='ver_contratos'),
    path('contratos/agregar/', views.agregar_contrato, name='agregar_contrato'),
    path('contratos/actualizar/<int:contrato_id>/', views.actualizar_contrato, name='actualizar_contrato'), # NUEVA URL
    path('contratos/borrar/<int:contrato_id>/', views.borrar_contrato, name='borrar_contrato'), # NUEVA URL
]