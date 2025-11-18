from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100) # Corregido Charfield a CharField
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} {self.apellido}" # Corregido __srt__ a __str__

# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.puesto})"

# ==========================================
# MODELO: SERVICIO
# ==========================================
class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion_estimada_horas = models.DecimalField(max_digits=4, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    tipo_servicio = models.CharField(max_length=50, help_text="Ej: Poda, Riego, Diseño, Fumigación")

    def __str__(self):
        return self.nombre_servicio

# ==========================================
# MODELO: CONTRATOSERVICIO
# (Relación de 1 a muchos: Un cliente puede tener muchos contratos de servicio)
# (Relación de muchos a muchos: Un contrato de servicio puede ser realizado por varios empleados, y un empleado puede participar en varios contratos)
# ==========================================
class ContratoServicio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contratos')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='contratos')
    empleados = models.ManyToManyField(Empleado, related_name='servicios_asignados')
    fecha_contrato = models.DateField(auto_now_add=True)
    fecha_programada = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=[
            ('PENDIENTE', 'Pendiente'),
            ('EN_PROGRESO', 'En Progreso'),
            ('COMPLETADO', 'Completado'),
            ('CANCELADO', 'Cancelado'),
        ],
        default='PENDIENTE'
    )
    observaciones = models.TextField(blank=True, null=True)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # Se puede calcular

    def __str__(self):
        return f"Contrato {self.id} - {self.cliente} - {self.servicio.nombre_servicio}"