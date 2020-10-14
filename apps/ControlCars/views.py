from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views.generic import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from apps.ControlCars.models import Carros
from apps.ControlCars.models import Clientes
from apps.ControlCars.models import VentaCars
from apps.ControlCars.models import Alquiler
from apps.ControlCars.models import Usuarios
from apps.ControlCars.forms import CarroForm 
from apps.ControlCars.forms import PersonaForm
from apps.ControlCars.forms import AlquilerForm
from apps.ControlCars.forms import VenderForm, VenderEditForm
from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
import io
from io import BytesIO
from django.conf import settings
from reportlab.platypus.tables import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.template.loader import get_template
# Create your views here.
# class In(TemplateView):
#     template_name = "base/index.html"

@login_required
def index(request):
    return render(request,'base/index.html')

def registro1(request):
    return render(request, 'crudpersonas/usuario.html')


def Reportes(request):
	ingresos = VentaCars.objects.all()
	context = {
	    'ventas': ingresos,
	}
	return render(request, 'Reportes/reportes.html',context)


@login_required


def get_Reportes1_id(request):
    ''' Funcion para obtener id del egreso'''
    egreso = VentaCars.objects.all()
    
   
    egreso_list = serializers.serialize('json', egreso)
    return JsonResponse(egreso_list, safe=False)

def get_Reportes2_id(request):
    ''' Funcion para obtener id del egreso'''
    egreso = Alquiler.objects.all()
    
   
    egreso_list = serializers.serialize('json', egreso)
    return JsonResponse(egreso_list, safe=False)
 


class CarroCrear(CreateView):
	model=Carros
	form_class=CarroForm
	template_name="crudcarros/fCarros.html"
	success_url= reverse_lazy('cars:carlistar')

class CarroListar(ListView):
	queryset= Carros.objects.order_by('id')
	template_name="crudcarros/ListaCar.html"

class CarroUpdate(UpdateView):
	model=Carros	
	form_class=CarroForm
	template_name="crudcarros/fCarros.html"
	success_url= reverse_lazy('cars:carlistar')

class CarroDelete(DeleteView):
	model=Carros
	template_name="crudcarros/deleteCar.html"
	success_url= reverse_lazy('cars:carlistar')


class PersonaCrear(CreateView):
	model=Clientes
	form_class=PersonaForm
	template_name="crudpersonas/fPersona.html"
	success_url= reverse_lazy('cars:perlist')

class PersonaListar(ListView):
	queryset= Clientes.objects.order_by('id')
	template_name="crudpersonas/ListaPer.html"


class PersonaUpdate(UpdateView):
	model=Clientes
	form_class=PersonaForm
	template_name="crudpersonas/fPersona.html"
	success_url= reverse_lazy('cars:perlist')


class PersonaDelete(DeleteView):
	model=Clientes
	template_name="crudpersonas/deletePersona.html"
	success_url= reverse_lazy('cars:perlist')

def registro(request):
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    user_name = request.POST.get('username')
  
    password = request.POST.get('password')
    #imagen = request.FILES.get('img_perfil')
    print("la imagen de registro")
    #print(imagen)
    user = User.objects.create_user(
        first_name = nombre,
        last_name = apellido,
        password = password,
        username = user_name,
    )
    user.save()
    usuario = Usuarios(
        user = user,
    )
    usuario.save()
   # enviarCorreo(email)
    
    return redirect('cars:index')



@login_required
def AlquilerCrear(request):
	form_class=AlquilerForm()

	if request.method=='POST':
	   form_class=AlquilerForm(request.POST or None, request.FILES or None)
	   if form_class.is_valid():
	   	id_carro=request.POST.get('carro')
	   	print("el id carro es",id_carro)
	   	carro=Carros.objects.get(id=id_carro)
	   	form_class.save()
	   	venta=Alquiler.objects.last()
	   	venta.idcar=carro
	   	venta.save()
	   	carro.EstadoAlquiler=True
	   	carro.save()
	   	return redirect('cars:alquilerlista')

	Carross= Carros.objects.filter(EstadoAlquiler=False,EstadoVenta=False)
	context={'carros':Carross,'form':form_class}
	return render(request, 'alquiler/fAlquiler.html',context)

@login_required
def DevolverAlquiler(request,pk):
	detalles=Alquiler.objects.get(id=pk)
	detalles.terminado=False
	detalles.save()
	carro=Carros.objects.get(placa=detalles.idcar)
	carro.EstadoAlquiler=False
	carro.save()
	return redirect('cars:alquilerlista')

	


@login_required
def AlquilerListar(request):
    ingresos = Alquiler.objects.all()
    ingreso_form =  AlquilerForm
    context = {
        'alquiler': ingresos,
        'form': ingreso_form
    }
    return render (request, 'alquiler/Listaalquiler.html', context)

@login_required
def get_alquiler_id(request, pk):
    ''' Funcion para obtener id del egreso'''
    egreso = Alquiler.objects.filter(id=pk)
    egreso_list = serializers.serialize('json', egreso)
    return HttpResponse(egreso_list, content_type="text/json-comment-filtered")

class AlquilerUpdate(UpdateView):
	model=Alquiler
	form_class=AlquilerForm
	template_name="alquiler/fAlquiler.html"
	success_url= reverse_lazy('cars:alquilerlista')


@login_required
def AlquilerDelete(request,pk):
	detalles=Alquiler.objects.get(id=pk)
	
	carro=Carros.objects.get(placa=detalles.idcar)
	carro.EstadoAlquiler=False
	carro.save()
	detalles.delate()
	return redirect('cars:alquilerlista')

class Pff(DeleteView):
	model=Alquiler
	template_name="factura/FacAlqui.html"

@login_required
def some_view(request):
	model=Alquiler
	buffer = io.BytesIO()
	p = canvas.Canvas(buffer)
	p.drawString(100, 100, "Hello world.")
	p.showPage()
	p.save()
	buffer.seek(0)
	return FileResponse(buffer, as_attachment=True, filename='hello.pdf')



@login_required
def VenderCrear(request):
	form_class=VenderForm()

	if request.method=='POST':
	   form_class=VenderForm(request.POST or None, request.FILES or None)
	   if form_class.is_valid():
	   	id_carro=request.POST.get('carro')
	   	print("el id carro es",id_carro)
	   	carro=Carros.objects.get(id=id_carro)
	   	form_class.save()
	   	venta=VentaCars.objects.last()
	   	venta.idcar=carro
	   	venta.save()
	   	carro.EstadoVenta=True
	   	carro.save()
	   	return redirect('cars:listaventa')

	Carross= Carros.objects.filter(EstadoVenta=False,EstadoAlquiler=False)
	context={'carros':Carross,'form':form_class}
	return render(request, 'Vender/fVender.html',context)





class simulador(TemplateView):
    template_name = "Vender/simulador.html"
	


@login_required
def VenderListar(request):
    ingresos = VentaCars.objects.all()
    ingreso_form =  VenderEditForm
    context = {
        'ventas': ingresos,
        'form': ingreso_form
    }
    return render (request, 'Vender/listarVenta.html', context)

@login_required
def guardar_editado(request):
# funcion para guar lo editado de la venta
	pk_venta = request.POST.get('id_Venta')
	pk_car_ant = request.POST.get('pk_car_ant')
	carro_ant = Carros.objects.get(id=pk_car_ant)
	placa_ant = carro_ant.placa
	print(placa_ant)
	venta = VentaCars.objects.get(id=pk_venta)
	egreso_form = VenderEditForm(instance = venta)
	if request.method == 'POST':
		egreso_form = VenderEditForm(request.POST, instance=venta)
		if egreso_form.is_valid():
			venta = egreso_form.save(commit=False)
			venta.save()
			venta_aux = VentaCars.objects.last()
			carro = venta_aux.idcar
			carro_nuevo = Carros.objects.get(placa=carro)
			if placa_ant != carro:
				carro_ant.EstadoVenta = False
				carro_ant.save()
				carro_nuevo.EstadoVenta = True
				carro_nuevo.save()
	return redirect('cars:listaventa')

class VenderUpdate(UpdateView):
	model=VentaCars
	form_class=VenderForm
	template_name="Vender/fVender.html"
	success_url= reverse_lazy('cars:listaventa')

class VenderDelete(DeleteView):
	model=VentaCars
	template_name="Vender/borrarvender.html"
	success_url= reverse_lazy('cars:listaventa')

@login_required
def get_venta_id(request, pk):
    ''' Funcion para obtener id del egreso'''
    egreso = VentaCars.objects.filter(id=pk)
    egreso_list = serializers.serialize('json', egreso)
    return HttpResponse(egreso_list, content_type="text/json-comment-filtered")


class VentasPersonasPDF(ListView):

	

	def cabecera(self,pdf):
		
		pdf.setFont("Helvetica", 25)
		pdf.drawString(160, 790, u"DOCUMENTO PRIVADO")

	def get(self, request, *args, **kwargs):
		response = HttpResponse(content_type='application/pdf')
		buffer = BytesIO()
		pdf = canvas.Canvas(buffer)
		self.cabecera(pdf)
		pdf.showPage()
		pdf.save()
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response


	def tabla(self,pdf,y,pk):
		model=VentaCars
		detalles=VentaCars.objects.get(id=pk)
		pdf.setFont("Helvetica", 12)
		pdf.drawString(20,760, u"PRIMERO: Interviene en el presente contrato por una parte el Sr(a): Esteban Jose Bravo Cueva")
		pdf.drawString(20,740, u"Con c.c:   1102222222       Vive en: Carimanga Loja Ecuador")
		pdf.drawString(20,720, u"Telefono: 0988323380     Que se demomina vendedor y por otra parte el Sr(a): "+detalles.idcliente.NombreyApellido)
		pdf.drawString(20,700, u"Con c.c: "+detalles.idcliente.Cedula +"     Que se demomina comprador")
		pdf.drawString(20,670, u"SEGUNDA: antecedentes Sr. Esteban Jose Bravo Cueva")
		pdf.drawString(20,650, u"Vende el vehiculo marca: "+detalles.idcar.marca)
		pdf.drawString(300,650, u"Placa: "+detalles.idcar.placa)
		pdf.drawString(20,630, u"Color: "+detalles.idcar.Color)
		pdf.drawString(150,630, u"Clase: "+detalles.idcar.Clase)
		pdf.drawString(300,630, u"Tipo: "+detalles.idcar.Tipo)
		pdf.drawString(20,610, u"Modelo: "+detalles.idcar.modelo)
		pdf.drawString(20,580, u"Matriculado en: "+detalles.idcar.MatriculadoEn)
		pdf.drawString(20,550, u"TERCERA: el precio de venta del vehiculo es de: "+detalles.PrecioVenta)
		pdf.drawString(20,520, u"Que es cancelado de la siguiente manera: comprador : "+detalles.TipodeVenta)
		pdf.drawString(20,490, u"Ademas el comprador se compromete a realizar la documentacion en cierta fecha : "+detalles.Fecha_Documentacion.strftime("%D:%M:%Y"))
		pdf.drawString(20,460, u"El vendedor declara que el vehiculo materia de la presente venta se encuentra en perfecto estado y ")
		pdf.drawString(20,445, u"funcionando, en el mismo entregandose todos y cada uno de los accesorios que se encuentran en el  ")
		pdf.drawString(20,430, u"mismo previo el respectivo chequeo e inspeccion por parte del comprador, asi como tambien declara ")
		pdf.drawString(20,415, u"que sobre el vehiculo no posee ningún gravamen que perita la venta, asi como también el comprador ")
		pdf.drawString(20,400, u"se hace responsable de todo lo que pase posteriormente dado los siguientes puntos se hace un acuerdo")
		pdf.drawString(20,385, u"entre los involucrados en el presente documento sobre la cancelacion de multas y sanciones cometidas")
		pdf.drawString(20,370, u"a partir de la fecha expuesta en este documento responsabilizandose el infractor a su cancelación.")
		pdf.drawString(20,335, u"Por otra parte en caso que se desita del negocio en las primeras 24 horas se comprometen a cancelar")
		pdf.drawString(20,320, u"$1000 dolares americanos en efectivo")

		pdf.setFont("Helvetica", 14)
		pdf.drawString(20,300, u"OBSERVACIONES:")
		pdf.drawString(20,280, u""+detalles.descripcionA)

		pdf.setFont("Helvetica", 12)
		pdf.drawString(20,120, u"Para constancia de lo actuado las partes contratantes firman en el presente documento y adjuntan la")
		pdf.drawString(20,105, u"doc respectiva en la ciudad de "+detalles.CiudadVenta +"a los fecha "+ detalles.Fecha_Venta.strftime("%D:%M:%Y"))
		pdf.drawString(100,20, u"VENDEDOR")
		pdf.drawString(400,20, u"COMPRADOR")



	def get(self, request, *args, **kwargs):
		response = HttpResponse(content_type='application/pdf')
		buffer = BytesIO()
		pdf = canvas.Canvas(buffer)
		self.cabecera(pdf)
		y = 600
		pk=kwargs['pk']
		print(pk)
		self.tabla(pdf, y,pk)
		pdf.showPage()
		pdf.save()
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response

class ReportePersonasPDF(ListView):

	

	def cabecera(self,pdf):
		
		pdf.setFont("Helvetica", 42)
		pdf.drawString(160, 790, u" GB MOTOR'S")
		archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logoGB.png'
		pdf.drawImage(archivo_imagen, 200, 460, 160, 500,preserveAspectRatio=True)

	def get(self, request, *args, **kwargs):
		response = HttpResponse(content_type='application/pdf')
		buffer = BytesIO()
		pdf = canvas.Canvas(buffer)
		self.cabecera(pdf)
		pdf.showPage()
		pdf.save()
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response


	def tabla(self,pdf,y,pk):
		encabezados = ('Nombre', 'Placa', 'Dia', 'Valor')
		model=Alquiler
		detalles=Alquiler.objects.get(id=pk)
		pdf.setFont("Helvetica", 12)
		pdf.drawString(60,600, u" Nombre Cliente: "+detalles.idcliente.NombreyApellido)
		pdf.drawString(60,570, u" Telefono Celular: "+detalles.idcliente.Celular)
		pdf.drawString(60,540, u" Fecha de Salida: "+detalles.Fecha_Salida.strftime("%D:%M:%Y"))
		pdf.drawString(300,540, u" Fecha de Entrega: "+detalles.F_Entrega.strftime("%D:%M:%Y"))
		pdf.drawString(60,510, u" Codigo de Alarma: "+detalles.idcar.Codigo)
		pdf.drawString(60,480, u" Vehiculo: "+detalles.idcar.marca +"  "+detalles.idcar.modelo )
		pdf.drawString(300,480, u" Placa: "+detalles.idcar.placa)
		pdf.drawString(60,450, u" Llantas: "+detalles.llantas)
		pdf.drawString(300,450, u" Pintura: "+detalles.pintura)
		pdf.drawString(60,420, u" Luces: "+detalles.luces)
		pdf.drawString(300,420, u" Kilometraje: "+detalles.kmActual)
		pdf.drawString(60,390, u" Motor: "+detalles.motor)
		pdf.drawString(300,390, u" Caja: "+detalles.cajas)
		pdf.drawString(60,360, u" Valor: "+detalles.valor)
		pdf.drawString(60,330, u" Descripción: ")
		pdf.drawString(60,300, u""+detalles.descripcionA)
		pdf.drawString(250,250, u" Firma Cliente")
		pdf.drawString(60,150, u" Recibido por: --------------------------------------------------------")
	
		

	def get(self, request, *args, **kwargs):
		response = HttpResponse(content_type='application/pdf')
		buffer = BytesIO()
		pdf = canvas.Canvas(buffer)
		self.cabecera(pdf)
		y = 600
		pk=kwargs['pk']
		print(pk)
		self.tabla(pdf, y,pk)
		pdf.showPage()
		pdf.save()
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response




class ReportesFuturosPDF(View):
	def cabecera(self,pdf):
		
		pdf.setFont("Helvetica", 36)
		pdf.drawString(160, 790, u" GB MOTOR'S")
		pdf.setFont("Helvetica", 14)
		pdf.drawString(200, 770, u"REPORTE DE VENTAS")
		archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logoGB.png'
		pdf.drawImage(archivo_imagen, 200, 460, 160, 500,preserveAspectRatio=True)

	def get(self, request, *args, **kwargs):
		response = HttpResponse(content_type='application/pdf')
		buffer = BytesIO()
		pdf = canvas.Canvas(buffer)
		self.cabecera(pdf)
		pdf.showPage()
		pdf.save()
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response


	def tabla(self,pdf,y):
		encabezados = ('Nombre', 'Placa', 'Dia', 'Valor')
		model=Alquiler
		
		detalles = [(persona.idcliente,persona.idcar,persona.Fecha_Salida,  persona.valor) for persona in model.objects.filter()]
		detalle_orden = Table([encabezados] + detalles, colWidths=[2 *cm, 5 *cm, 5 *cm, 5 *cm])
		detalle_orden.setStyle(TableStyle(
			[
			('ALIGN',(0,0),(3,0),'CENTER'),
			('GRID', (0, 0), (-1, -1), 1, colors.black),
			('FONTSIZE', (0, 0), (-1, -1), 10),
			]
			))
		detalle_orden.wrapOn(pdf, 800, 600)
		detalle_orden.drawOn(pdf, 60,y)


	def get(self, request, *args, **kwargs):
		response = HttpResponse(content_type='application/pdf')
		buffer = BytesIO()
		pdf = canvas.Canvas(buffer)
		self.cabecera(pdf)
		y = 600
		self.tabla(pdf, y)
		pdf.showPage()
		pdf.save()
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response
