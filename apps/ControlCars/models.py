from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Carros(models.Model):
	"""docstring for Carros"""
	id=models.AutoField(primary_key=True)
	marca=models.CharField(max_length=20)
	modelo=models.CharField(max_length=20)
	descripcion=models.CharField(max_length=1000)
	placa=models.CharField(max_length=20)
	extra=models.CharField(max_length=20)
	Codigo=models.CharField(max_length=20)
	FechaCompra=models.DateField()
	DuenoA=models.CharField(max_length=20)
	Chasis=models.CharField(max_length=20)
	Tipo=models.CharField(max_length=20)
	Motor=models.CharField(max_length=20)
	PrecioCompra=models.CharField(max_length=20)
	Color=models.CharField(max_length=20)
	Clase=models.CharField(max_length=20)
	MatriculadoEn=models.CharField(max_length=20)
	EstadoVenta=models.BooleanField(default=False)
	EstadoAlquiler=models.BooleanField(default=False)
	def __str__(self):
		return '{}'.format(self.placa)



class Clientes(models.Model):
	"""docstring for Carros"""
	id=models.AutoField(primary_key=True)
	NombreyApellido=models.CharField(max_length=100)
	Cedula=models.CharField(max_length=20)
	Celular=models.CharField(max_length=20)
	def __str__(self):
		return '{}'.format(self.NombreyApellido)

class Alquiler(models.Model):
	id=models.AutoField(primary_key=True)
	idcar=models.ForeignKey(Carros, null=True, blank=True, on_delete=models.CASCADE)
	idcliente=models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.CASCADE)
	Fecha_Salida=models.DateField()
	F_Entrega=models.DateField()
	llantas=models.CharField(max_length=20)
	motor=models.CharField(max_length=20)
	pintura=models.CharField(max_length=20)
	luces=models.CharField(max_length=20)
	kmActual=models.CharField(max_length=20)
	valor=models.CharField(max_length=20)
	descripcionA=models.CharField(max_length=1000)
	cajas=models.CharField(max_length=20)
	terminado=models.BooleanField(default=True)
	def __str__(self):
		return '{}'.format(self.motors)

class VentaCars(models.Model):
	id=models.AutoField(primary_key=True)
	idcar=models.ForeignKey(Carros, null=True, blank=True, on_delete=models.CASCADE)
	idcliente=models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.CASCADE)
	MatriculadoPor=models.CharField(max_length=100)
	PrecioVenta=models.CharField(max_length=20)
	TipodeVenta=models.CharField(max_length=100)
	Fecha_Documentacion=models.DateField()
	CiudadVenta=models.CharField(max_length=100)
	Fecha_Venta=models.DateField()
	descripcionA=models.CharField(max_length=1000)
	def __str__(self):
		return '{}'.format(self.MatriculadoPor)

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    

    class Meta:
        verbose_name = "usuarios"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.user.username