from django.http import HttpResponse,JsonResponse
from django.conf.urls import url
from apps.ControlCars.views import CarroCrear,CarroListar,CarroUpdate,CarroDelete,PersonaCrear,PersonaListar,PersonaDelete,PersonaUpdate,AlquilerCrear,AlquilerListar,AlquilerUpdate,AlquilerDelete,Pff,some_view,ReportePersonasPDF,VenderCrear,VenderListar, VenderDelete,VenderUpdate,VentasPersonasPDF,simulador,DevolverAlquiler,registro,get_Reportes1_id,get_Reportes2_id
from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = 'main_app'
urlpatterns = [
    # url   (r'^index', In.as_view(),name='index'),
   path('index', views.index, name='index'),
   path('regis', views.registro1, name='regis'),
   path('reportes', views.Reportes, name='reportes'),

   url(r'^get_reportes_id/',get_Reportes1_id,name = 'get_reportes_id'),
   url(r'^get_reportes2_id/',get_Reportes2_id,name = 'get_reportes2_id'),


   path('get_alquiler_id/<int:pk>', views.get_alquiler_id, name = 'get_alquiler_id'),

    path('',auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='base/login.html'), name='logout'),


    path('registro/', views.registro, name = 'registro'),



    url(r'^nuevo/',CarroCrear.as_view(), name='carro_crear'),
    url(r'^listar/',CarroListar.as_view(), name='carlistar'),
    url(r'^eliminar/(?P<pk>\d+)/$',CarroDelete.as_view(), name='carEliminar'),
    url(r'^editar/(?P<pk>\d+)/$',CarroUpdate.as_view(), name='carEditar'),
    url(r'^cliNuevo/',PersonaCrear.as_view(), name='pernuevo'),
    url(r'^cliListar/',PersonaListar.as_view(), name='perlist'),
    url(r'^eliminarcli/(?P<pk>\d+)/$',PersonaDelete.as_view(), name='cliEliminar'),
    url(r'^editarcli/(?P<pk>\d+)/$',PersonaUpdate.as_view(), name='cliEditar'),
    
    url(r'^nuevoalq/$',views.AlquilerCrear, name='nuevoalquiler'),



    url(r'^listaalq/$',views.AlquilerListar, name='alquilerlista'),
    url(r'^guardar_editado/$',views.guardar_editado, name='guardar_editado'),
    path('get_alquiler_id/<int:pk>', views.get_alquiler_id, name = 'get_alquiler_id'),

     url(r'^eliminaralq/(?P<pk>\d+)/$',views.AlquilerDelete, name='eliminaralq'),



    url(r'^devolver/(?P<pk>\d+)/$',views.DevolverAlquiler, name='devolver'),




    url(r'^editaralq/(?P<pk>\d+)/$',AlquilerUpdate.as_view(), name='editarq'),
    url(r'^reporte_personas_pdf/(?P<pk>\d+)/$',ReportePersonasPDF.as_view(), name="reporte_personas_pdf"),
    url(r'^nuevaventa/$',views.VenderCrear, name='nuevaventa'),
    url(r'^eliminarventa/(?P<pk>\d+)/$',VenderDelete.as_view(), name='eliminarventa'),
    url(r'^editarventa/(?P<pk>\d+)/$',VenderUpdate.as_view(), name='editarventa'),
    path('get_venta_id/<int:pk>', views.get_venta_id, name = 'get_venta_id'),



    url(r'^listaventa/$',views.VenderListar, name='listaventa'),
    url(r'^doc_ventas_pdf/(?P<pk>\d+)/$',VentasPersonasPDF .as_view(), name="doc_ventas_pdf"),
    url(r'^simulador/',simulador.as_view(), name='simulador'),

]