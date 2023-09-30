from django.db import models

class Repartidor(models.Model):
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    nombre_apellido_repartidor = models.CharField(max_length=50, unique=True)
    mail_repartidor = models.EmailField(max_length=100, unique=True)
    direccion_repartidor = models.CharField(max_length=100)
    fecha_nacimiento_repartidor = models.DateField()
    fecha_registro_repartidor = models.DateField()
    edad_repartidor = models.PositiveIntegerField()
    genero = models.CharField(max_length=1)
    status_repartidor = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nombre_apellido_repartidor

class Tienda(models.Model):
    ZONA_CHOICES = [
        ('Recoleta', 'Recoleta'),
        ('Caballito', 'Caballito'),
        ('Almagro', 'Almagro'),
        ('Colegiales', 'Colegiales'),
    ]

    titular_tienda = models.CharField(max_length=50)
    denominacion_social_tienda = models.CharField(max_length=100, unique=True)
    direccion_tienda = models.CharField(max_length=30)
    telefono_tienda = models.IntegerField()
    zona_tienda = models.CharField(max_length=10, choices=ZONA_CHOICES)
    mail_tienda = models.CharField(max_length=50)

    def __str__(self):
        return self.denominacion_social_tienda

class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('Alimentos y bebidas', 'Alimentos y bebidas'),
        ('Farmacia y cuidado personal', 'Farmacia y cuidado personal'),
        ('Hogar', 'Hogar'),
    ]

    nombre_producto = models.CharField(max_length=40, unique=True)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.nombre_producto

class Pago(models.Model):
    METODO_PAGO_CHOICES = [
        ('Tarjeta de credito', 'Tarjeta de crédito'),
        ('Tarjeta de debito', 'Tarjeta de débito'),
        ('Efectivo', 'Efectivo'),
    ]

    fecha_pago = models.DateField()
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES)
    monto = models.IntegerField()

    def __str__(self):
        return f"Pago {self.id} - {self.fecha_pago}"
    
class Usuario(models.Model):
    nombre_apellido_usuario = models.CharField(max_length=50, unique=True)
    mail_usuario = models.EmailField(max_length=100, unique=True)
    telefono_usuario = models.IntegerField()
    direccion_usuario = models.CharField(max_length=50)
    edad_usuario = models.IntegerField()
    genero = models.CharField(max_length=1)
    zona = models.CharField(max_length=50)
    fecha_registro_usuario = models.DateField()

    def __str__(self):
        return self.nombre_apellido_usuario
    

class Cancelacion(models.Model):
    MOTIVO_CANCEL_CHOICES = [
        ('Falta disponibilidad repartidor', 'Falta disponibilidad repartidor'),
        ('Cancelacion del usuario', 'Cancelacion del usuario'),
        ('Mal tiempo', 'Mal tiempo'),
        ('Cancelacion de la tienda', 'Cancelacion de la tienda'),
    ]

    motivo_cancel = models.CharField(max_length=50, choices=MOTIVO_CANCEL_CHOICES)
    costo_cancel = models.IntegerField()
    fecha_cancel = models.DateField()
    hora_cancel = models.TimeField()

    def __str__(self):
        return f"Cancelación {self.id} - {self.motivo_cancel}"
    
class Orden(models.Model):
    STATUS_ORDEN_CHOICES = [
        ('Entregada', 'Entregada'),
        ('Cancelada', 'Cancelada'),
    ]

    id_repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE)
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_pago = models.OneToOneField(Pago, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_cancel = models.ForeignKey(Cancelacion, on_delete=models.CASCADE)
    fecha_orden = models.DateField()
    status_orden = models.CharField(max_length=20, choices=STATUS_ORDEN_CHOICES)
    hora_entrega_orden = models.TimeField()

    def __str__(self):
        return f"Orden {self.id} - {self.status_orden}"
    