from django.conf.urls import url, include
from django.contrib import admin
#VISTAS Inicio de sesion
from django.contrib.auth import views as auth_views
from Apps.Acordemos.views import salir
#VISTAS Inicio
from Apps.Acordemos.views import infoBase
#VISTAS Lista de acuerdos /Subida y Descarga
from Apps.Acordemos.views import listaAcuerdos, subir_Acta, borrar_Acta
#VISTAS Perfil
from Apps.Acordemos.views import perfil
#VISTAS Crear Convocatoria
from Apps.Acordemos.views import crear_convocatoria
#VISTAS Mis Reuniones
from Apps.Acordemos.views import eliminar_reunion,reunion_list, agregar_invitados, eliminar_invitado, CrearTema, menuTema, crear_archivo, asignarEnlace, eliminar_tema, reunion_editar,enviarCorreo,resumen
#VISTAS Acordemos
from Apps.Acordemos.views import acordemos,pasarAsistencia,eliminar_asistencia,acuerdo_crear,comentarios,votacion,acuerdo_editar,pdf

urlpatterns = [
    #URL del administrador
    url(r'^admin/', admin.site.urls),
    #URL's de inicio sesion de usuario
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^salir/$', salir, name='salir'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    #INICIO
    url(r'^$', infoBase, name='home'),
    #Lita de Acuerdos || Subir y Descargar actas
    url(r'Lista_Acuerdos/$', listaAcuerdos, name='acuerdoLista'),
    url(r'Lista_Acuerdos/(?P<acuerdo_id>\d+)/$', subir_Acta, name='subirActa'),
    url(r'Lista_Acuerdos/eliminar/(?P<acta_id>\d+)/$', borrar_Acta, name='borrarActa'),
    # Perfil(miembros de alguna comision)
    url(r'^Perfil/$', perfil, name='perfil'),
    #:::Aplicaciones de Secretario O Presidente:::
    #           Crear Convocatoria
    url(r'^Crear_Convocatoria/(?P<user_id>\d+)/$', crear_convocatoria, name='registroReunion'),                     #CREAR CONVOCATORIA
    #           Mis Reuniones
    url(r'^Mis_Reuniones/$', reunion_list, name='reunionlista'),                                                    #MIS REUNIONES
    url(r'^Mis_Reuniones/resumen/(?P<reunion_id>\d+)/$', resumen, name='resumenAcuerdos'),
    url(r'^Mis_Reuniones/agregar_Invitados/(?P<reunion_id>\d+)/$', agregar_invitados, name='registroInvitados'),    #Agragar Invitado
    url(r'^Mis_Reuniones/invitado/eliminar/(?P<invitado_id>\d+)/$', eliminar_invitado, name='eliminarInvitados'),   #Eliminar Invitado
    url(r'^Mis_Reuniones/nuevoTema/(?P<reunion_id>\d+)/$', CrearTema, name='newTema'),                              #Crear Nuevo Tema
    url(r'Mis_Reuniones/Tema/Informacion/(?P<tema_id>\d+)/$', menuTema, name='menuTema'),                           #Opciones del Tema
    url(r'^Mis_Reuniones/agregar_Tema/Archivo/(?P<tema_id>\d+)/$', crear_archivo, name='crearArchivo'),             #AGREGAR Archivo
    url(r'^Mis_Reuniones/agregar_Tema/Enlace/(?P<tema_id>\d+)/$', asignarEnlace, name='crearEnlace'),               #AGREGAR Enlace
    url(r'^Mis_Reuniones/tema/eliminar/(?P<tema_id>\d+)/$', eliminar_tema, name='eliminarTema'),                    #Eliminar Tema
    url(r'^Mis_Reuniones/editar/(?P<reunion_id>\d+)/$', reunion_editar, name='editarReunion'),                      #Editar Reunion
    url(r'^Mis_Reuniones/eliminar/(?P<reunion_id>\d+)/$', eliminar_reunion, name='eliminarReunion'),                #Eliminar Reunion
    url(r'^Mis_Reuniones/enviar/(?P<reunion_id>\d+)/$', enviarCorreo, name='enviarCorreo'),                         #Enviar Convocatoria(invitados)
    #           Acordemos
    url(r'^Mis_Reuniones/Acordemos/(?P<reunion_id>\d+)/$', acordemos, name='acordemos'),                            #Acordemos (Por Reunion)
    url(r'^Mis_Reuniones/Acordemos/asistencia/(?P<integrante_id>\d+)/(?P<reunion_id>\d+)/$', pasarAsistencia, name='pasarAsistencia'), #Asistencia
    url(r'^Mis_Reuniones/Acordemos/asistencia/eliminar/(?P<asistencia_id>\d+)/(?P<reunion_id>\d+)/$', eliminar_asistencia, name='eliminarAsistencia'), #eliminarAsistencia
    url(r'^Mis_Reuniones/Acordemos/crear_acuerdo/(?P<tema_id>\d+)/(?P<reunion_id>\d+)/$', acuerdo_crear, name='crearacuerdo'),         #Acordar por Tema
    url(r'^Mis_Reuniones/Acordemos/comentarios/(?P<asistencia_id>\d+)/(?P<acuerdo_id>\d+)/(?P<reunion_id>\d+)/$', comentarios, name='comentariosAcuerdos'),      # COMENTARIOS
    url(r'^Mis_Reuniones/Acordemos/votacion/(?P<asistencia_id>\d+)/(?P<acuerdo_id>\d+)/(?P<reunion_id>\d+)/$', votacion, name='votacionAcuerdo'),                # VOTACION
    url(r'^Mis_Reuniones/Acordemos/acuerdo/(?P<reunion_id>\d+)/(?P<acuerdo_id>\d+)/$', acuerdo_editar, name='editarAcuerdo'),  #Cambiar Estado del Acuerdo(segun la votacion realizada)
    url(r'^Mis_Reuniones/Acordemos/generarPDF/(?P<reunion_id>\d+)/$', pdf, name='generarPDF'),                      #Generar PDF
]
