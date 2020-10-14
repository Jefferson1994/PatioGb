from django import forms
from apps.ControlCars.models import Carros
from apps.ControlCars.models import Clientes
from apps.ControlCars.models import Alquiler
from apps.ControlCars.models import VentaCars
class CarroForm(forms.ModelForm):
	class Meta:
		model=Carros
		fields=[
		  
		  'marca',
		  'modelo',
		  'placa',
		  'extra',
		  'Codigo',
		  'FechaCompra',
		  'DuenoA',
		  'Chasis',
		  'Tipo',
		  'Motor',
		  'Color',
		  'Clase',
		  'MatriculadoEn',
		  'PrecioCompra',
		  'descripcion',

		]

		labels={
		  
		  'marca':'Marca del auto',
		  'modelo':'Modelo del auto',
		  'placa':'Placa del auto',
		  'extra':'Gastos Extras',
		  'Codigo':'Codigo de Alarma',
		  'FechaCompra':'Fecha de compra',
		  'DuenoA':'Nombres del Dueño Anterior',
		  'Chasis':'Numero de chasis',
		  'Tipo': 'Tipo de vehiculo',
		  'Motor':'Cilindraje',
		  'Color':'Color',
		  'Clase':'Clase',
		  'MatriculadoEn':'Matriculado en',
		  'PrecioCompra':'Precio de Compra',
		  'descripcion':'Descripción',

		}

		widgets={

		  
		  'marca':forms.TextInput(attrs={'class':'form-control'}),
		  'modelo':forms.TextInput(attrs={'class':'form-control'}),
		  'placa':forms.TextInput(attrs={'class':'form-control'}),
		  'extra':forms.TextInput(attrs={'class':'form-control'}),
		  'Codigo':forms.TextInput(attrs={'class':'form-control'}),
		  'FechaCompra':forms.TextInput(attrs={'type':'date','class':'selectpicker'}),
		  'DuenoA':forms.TextInput(attrs={'class':'form-control'}),
		  'Chasis':forms.TextInput(attrs={'class':'form-control'}),
		  'Tipo':forms.TextInput(attrs={'class':'form-control'}),
		  'Motor':forms.TextInput(attrs={'class':'form-control'}),
		  'Color':forms.TextInput(attrs={'class':'form-control'}),
		  'Clase':forms.TextInput(attrs={'class':'form-control'}),
		  'MatriculadoEn':forms.TextInput(attrs={'class':'form-control'}),
		  'PrecioCompra':forms.TextInput(attrs={'class':'form-control'}),
		  
		  'descripcion':forms.Textarea(attrs={'class':'form-control' , 'maxlength':'6000'}),


		}

class PersonaForm(forms.ModelForm):
	class Meta:
		model=Clientes
		fields=[
		  
		  'NombreyApellido',
		  'Cedula',
		  'Celular',

		  
		]

		labels={
		  
		  'NombreyApellido':'Nombres y Apellido del  Cliente',
		  'Cedula':'Numero de Cedula',
		  'Celular':'Numero Movil',
		  
		}

		widgets={

		  
		  'NombreyApellido':forms.TextInput(attrs={'class':'form-control'}),
		  'Cedula':forms.TextInput(attrs={'class':'form-control'}),
		  'Celular':forms.TextInput(attrs={'class':'form-control'}),
		  
		}
			
class AlquilerForm(forms.ModelForm):
	class Meta:
		model=Alquiler
		exclude={'idcar'}
		fields=[

		
		'idcliente',
		'Fecha_Salida',
		'F_Entrega',
		'llantas',
		'motor',
		'pintura',
		'luces',
		'kmActual',
		'cajas',
		'descripcionA',
		'valor',
		]

		labels={
		  
		  
		  'idcliente':'Nombre Cliente',
		  'Fecha_Salida':'Fecha de Salida',
		  'F_Entrega':'Fecha de Entrega',
		  #'llantas':'Estado de las llantas',
		  'llantas':'Estado de las llantas?',
		  'motor':'Estado del motor',
		  'pintura':'Estado de la pintura',
		  'luces':'Estado de las luces',
		  'kmActual':'Kilometraje Actual',
		  'cajas':'Estado de la caja',
		  'descripcionA':'Descripción del Vehiculo',
		  'valor':'Valor',

		}
		EstadosCar= [
			('..', ''),
			('Si', 'Si'),
			('No', 'No'),
		]

		widgets={

		  
		  'idcliente':forms.Select(attrs={'class':'form-control'}),
		  'Fecha_Salida':forms.TextInput(attrs={'type':'date','class':'selectpicker'}),
		  'F_Entrega':forms.TextInput(attrs={'type':'date','class':'selectpicker'}),
		  #'llantas':forms.TextInput(attrs={'type':'select','class':'form-control'}),
		  'llantas':forms.Select(choices=EstadosCar,attrs={'class':'form-control'}),
		  #'motor':forms.TextInput(attrs={'class':'form-control'}),
		  'motor':forms.Select(choices=EstadosCar,attrs={'class':'form-control'}),
		  #'pintura':forms.TextInput(attrs={'class':'form-control'}),
		  'pintura':forms.Select(choices=EstadosCar,attrs={'class':'form-control'}),
		  #'luces':forms.TextInput(attrs={'class':'form-control'}),
		  'luces':forms.Select(choices=EstadosCar,attrs={'class':'form-control'}),
		  'kmActual':forms.TextInput(attrs={'class':'form-control'}),
		  #'cajas':forms.TextInput(attrs={'class':'form-control'}),
		  'cajas':forms.Select(choices=EstadosCar,attrs={'class':'form-control'}),
		  
		  'descripcionA':forms.Textarea(attrs={'class':'form-control' , 'maxlength':'6000'}),
		  'valor':forms.TextInput(attrs={'class':'form-control'}),
		  
		}
class VenderForm(forms.ModelForm):

	class Meta:
		model=VentaCars
		exclude={'idcar'}
		fields=[
		'idcliente',
		'MatriculadoPor',
		'PrecioVenta',
		'TipodeVenta',
		'Fecha_Documentacion',
		'CiudadVenta',
		'Fecha_Venta',
		'descripcionA',


		
		]

		labels={
		  
		  'idcliente':'Nombre Cliente',
		  'MatriculadoPor':'Matriculado Por',
		  'PrecioVenta':'Precio de Venta',
		  'TipodeVenta':'Tipo de Venta?',
		  'Fecha_Documentacion':'Fecha de Documentacion acordado con el Cliente',
		  'CiudadVenta':'Ciudad de Venta',
		  'Fecha_Venta':'Fecha de Venta',
		  'descripcionA':'Descripción de la venta del vehiculo',

		}
		TipoVenta= [
		    ('Efectivo', 'Efectivo'),
			('Financiado', 'Financiado'),
			('Abono', 'Abono'),
			('Saldo', 'Saldo'),
		]

		widgets={
		  'idcliente':forms.Select(attrs={'class':'form-control'}),
		  'MatriculadoPor':forms.TextInput(attrs={'class':'form-control'}),
		  'PrecioVenta':forms.TextInput(attrs={'class':'form-control'}),
		  'TipodeVenta':forms.Select(choices=TipoVenta,attrs={'class':'form-control'}),
		  'Fecha_Documentacion':forms.TextInput(attrs={'type':'date','class':'selectpicker'}),
		  'CiudadVenta':forms.TextInput(attrs={'class':'form-control'}),
		  'Fecha_Venta':forms.TextInput(attrs={'type':'date','class':'selectpicker'}),
		  
		  'descripcionA':forms.Textarea(attrs={'class':'form-control' , 'maxlength':'6000'}),
		  
		}

class VenderEditForm(forms.ModelForm):
	class Meta:
		model=VentaCars
		fields=[
			'idcar',
			'idcliente',
			'MatriculadoPor',
			'PrecioVenta',
			'TipodeVenta',
			'Fecha_Documentacion',
			'CiudadVenta',
			'Fecha_Venta',
			'descripcionA',]
		labels={
		  'idcar':'Placa',
		  'idcliente':'Nombre Cliente',
		  'MatriculadoPor':'Matriculado Por',
		  'PrecioVenta':'Precio de Venta',
		  'TipodeVenta':'Tipo de Venta?',
		  'Fecha_Documentacion':'Fecha de Documentacion acordado con el Cliente',
		  'CiudadVenta':'Ciudad de Venta',
		  'Fecha_Venta':'Fecha de Venta',
		  'descripcionA':'Descripción de la venta del vehiculo',

		}
		TipoVenta= [
		    ('Efectivo', 'Efectivo'),
			('Financiado', 'Financiado'),
			('Abono', 'Abono'),
			('Saldo', 'Saldo'),
		]

		widgets={
		  'idcliente':forms.Select(attrs={'class':'form-control'}),
		  'MatriculadoPor':forms.TextInput(attrs={'class':'form-control'}),
		  'PrecioVenta':forms.TextInput(attrs={'class':'form-control'}),
		  'TipodeVenta':forms.Select(choices=TipoVenta,attrs={'class':'form-control'}),
		  'Fecha_Documentacion':forms.TextInput(attrs={'type':'date','class':'selectpicker'}),
		  'CiudadVenta':forms.TextInput(attrs={'class':'form-control'}),
		  'Fecha_Venta':forms.TextInput(attrs={'type':'date','class':'selectpicker'}),
		  
		  'descripcionA':forms.Textarea(attrs={'class':'form-control' , 'maxlength':'6000'}),
		  
		}