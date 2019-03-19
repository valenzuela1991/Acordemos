# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Reunion, Integrante, Acuerdo, Tema, Comision, Asistencia, Votacion ,Invitado, Acta, Comentario
from .forms import ConvocatoriaForm, AcuerdoForm, InvitadosForm,  TemaForm , AsistenciaForm, ActaForm
from .forms import ComentarioForm ,ArchivoForm, EnlaceForm, VotacionForm
from .forms import acuerdoEstadoForm;
from .models import Enlace, Archivo
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
#mandar correo electronico a participants
from django.conf import settings
from django.core.mail import send_mail

# pip install Django==2.0.2
# pip install Django==2.0.2
# pip install Django==2.0.2
# pip install Django==2.0.2

#--------------------------------------------------------------
#----------------------CREAR CONVOCATORIA----------------------

from django.contrib.auth.models import User


def comentarioVotacion(request, reunion_id):
	reu = get_object_or_404(Reunion, pk=reunion_id)
	acuerdo = Acuerdo.objects.all()
	reunion = Reunion.objects.all()
	tema = Tema.objects.all()
	asistente = Asistencia.objects.all()
	integrante = Integrante.objects.all()
	return render(request, 'comision/comentarioVotacion.html',{'reu':reu,'reuniones':reunion,'temas':tema,'asistente':asistente,'acuerdo':acuerdo,'integrantes':integrante})


def pasarAsistencia(request, integrante_id, reunion_id):
	int = get_object_or_404(Integrante, pk = integrante_id)
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	if request.method == 'POST':
		form = AsistenciaForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.FK_Integrante_id = int.id
			post.FK_Reunion_id = reunion.id
			post.save()
			form.save()
		return redirect('../../../'+reunion_id)
	else:
		form = AsistenciaForm()
	return render(request, 'comision/asistencia_form.html', {'form':form, 'int':int,'reunion':reunion})


#	ELIMINAR asistente
def eliminar_asistencia(request, asistencia_id, reunion_id):
	asistencia = get_object_or_404(Asistencia, pk = asistencia_id)
	if request.method == 'POST':
		asistencia.delete()
		return redirect('../../../../'+reunion_id, asistencia_id)
	return render(request, 'comision/asistencia_delete.html', {'asistencia': asistencia})



#	AGREGAR INVITADOS
def agregar_invitados(request, reunion_id):
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	if request.method == 'POST':
		form = InvitadosForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.FK_Reunion_id = reunion.id
			post.save()
			form.save()
		return redirect('../../')
	else:
		form = InvitadosForm()
	return render(request, 'comision/invitados_form.html', {'form':form})


def eliminar_invitado(request, invitado_id):
		invitado = get_object_or_404(Invitado, pk = invitado_id)
		if request.method == 'POST':
			invitado.delete()
			return redirect('../../', invitado_id)
		return render(request, 'comision/reunion_delete.html', {'invitado': invitado})


from django.contrib import messages
#	CREAR CONVOCATORIA
def crear_convocatoria(request, user_id):
	integrante = Integrante.objects.filter(FK_User=user_id)
	for dato in integrante:
		comision = dato.FK_Comision
		if request.method == 'POST':
			form = ConvocatoriaForm(request.POST)
			if form.is_valid():
				post = form.save(commit=False)
				post.FK_Comision = comision
				post.save()
				form.save()
			return redirect('../../Mis_Reuniones/')
		else:
			form = ConvocatoriaForm()
		return render(request, 'comision/reunion_form.html',{'comision':comision,'form':form})


#	AGREGAR TEMA
def CrearTema(request, reunion_id):
	reu = get_object_or_404(Reunion, pk = reunion_id)
	if request.method == 'POST':
		form = TemaForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.FK_Reunion_id = reu.id
			post.save()
			form.save()
		return redirect('../../')
	else:
		form = TemaForm()
	return render(request, 'comision/newTema.html', {'form':form, 'reu':reu})


#			MENU DE TEMA
def menuTema(request, tema_id):
	temaID = get_object_or_404(Tema, pk = tema_id)
	return render (request, 'comision/verTemas.html',{'temaID':temaID})

#		ASIGNAR ENLACE
def asignarEnlace(request, tema_id):
	tema = get_object_or_404(Tema, pk = tema_id)
	if request.method == 'POST':
		form = EnlaceForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.FK_Tema_id = tema.id
			post.save()
			form.save()
		return redirect('../../../')
	else:
		form = EnlaceForm()
	return render(request, 'comision/enlace_form.html', {'form':form,'tema':tema})

#		ASIGNAR ARCHIVO
def crear_archivo(request, tema_id):
	tema = get_object_or_404(Tema, pk = tema_id)
	form = ArchivoForm(request.POST or None, request.FILES or None, request.POST or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.FK_Tema_id = tema.id
		post.save()
		form.save()
		return redirect('../../../')
	return render(request, "comision/archivo_form.html", {'form':form,'tema':tema})


def subir_Acta(request, acuerdo_id):
	acta = get_object_or_404(Acuerdo, pk = acuerdo_id)
	form = ActaForm(request.POST or None, request.FILES or None, request.POST or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.FK_Acuerdo_id = acta.id
		post.save()
		form.save()
		return redirect('../')
	return render(request, "comision/acta_subir.html", {'form':form,'acta':acta})

def borrar_Acta(request, acta_id):
	acta = get_object_or_404(Acta, pk= acta_id)
	if request.method == 'POST':
		acta.delete()
		return redirect('../../', acta_id)
	return render(request, 'comision/acta_delete.html', {'acta':acta})

#-------------------------------------------------------------
#------------------------MIS REUNIONES------------------------
#	LISTAR REUNIONES
def reunion_list(request):
	inv = Invitado.objects.all()
	integrante = Integrante.objects.all()
	archivo = Archivo.objects.all()
	reunion = Reunion.objects.all().order_by('id')
	comision = Comision.objects.all()
	tema = Tema.objects.all()
	enlace = Enlace.objects.all()
	acta = Acta.objects.all()
	votacion = Votacion.objects.all()
	acuerdos = Acuerdo.objects.all()
	acuerdoAceptado = Acuerdo.objects.filter(estado="Aceptado")
	comentarios = Comentario.objects.all()


	contexto = {'comentarios':comentarios,'acuerdoAceptado':acuerdoAceptado,'acuerdos':acuerdos,'votacion':votacion,'actas':acta,'inv':inv,'reuniones':reunion, 'temas':tema, 'integrantes':integrante, 'comisiones':comision,'enlaces':enlace,'archivos':archivo}
	return render(request, 'comision/reunion_lista.html', contexto)

def resumen(request, reunion_id):
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	inv = Invitado.objects.all()
	integrante = Integrante.objects.all()
	archivo = Archivo.objects.all()
	comision = Comision.objects.all()
	tema = Tema.objects.all()
	enlace = Enlace.objects.all()
	acta = Acta.objects.all()
	votacion = Votacion.objects.all()
	acuerdos = Acuerdo.objects.all()
	acuerdoAceptado = Acuerdo.objects.filter(estado="Aceptado")
	comentarios = Comentario.objects.all()

	contexto = {'comentarios':comentarios,'acuerdoAceptado':acuerdoAceptado,'acuerdos':acuerdos,'votacion':votacion,'actas':acta,'inv':inv,'reuniones':reunion, 'temas':tema, 'integrantes':integrante, 'comisiones':comision,'enlaces':enlace,'archivos':archivo}
	return render(request, 'comision/resumen.html', contexto)


#	EDITAR REUNIONES
def reunion_editar(request, reunion_id):
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	if request.method == 'GET':
		form = ConvocatoriaForm(instance=reunion)
	else:
		form = ConvocatoriaForm(request.POST, instance=reunion)
		if form.is_valid():
			form.save()
		return redirect('../../', reunion_id)
	return render(request, 'comision/reunionEditar.html', {'form':form})

#	ELIMINAR REUNIONES
def eliminar_reunion(request, reunion_id):
	reunion = get_object_or_404(Reunion, pk= reunion_id)
	if request.method == 'POST':
		reunion.delete()
		return redirect('../../', reunion_id)
	return render(request, 'comision/reunion_delete.html', {'reunion':reunion})

#	ELIMINAR Invitado
def eliminar_invitado(request, invitado_id):
		invitado = get_object_or_404(Invitado, pk = invitado_id)
		if request.method == 'POST':
			invitado.delete()
			return redirect('../../../', invitado_id)
		return render(request, 'comision/invitado_delete.html', {'invitado': invitado})

#	ELIMINAR Tema
def eliminar_tema(request, tema_id):
	tema = get_object_or_404(Tema, pk= tema_id)
	if request.method == 'POST':
		tema.delete()
		return redirect('../../../', tema_id)
	return render(request, 'comision/tema_delete.html', {'tema':tema})

#	Perfil
def perfil(request):
	comisiones = Comision.objects.all()
	integrantes = Integrante.objects.all()
	args = {'comisiones':comisiones,'integrantes':integrantes}
	return render(request, 'comision/perfil.html', args)

from django.core.mail import EmailMessage
#	Enviar correo a Invitados
def enviarCorreo(request, reunion_id):
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	integrantes = Integrante.objects.filter(FK_Comision=reunion.FK_Comision)
	archivo = Archivo.objects.all()
	invitado = Invitado.objects.all()
	tema = Tema.objects.all()
	reuniones = Reunion.objects.all()

	if request.method == 'POST':
		#ENVIAR CORREO INVITADOS
		for dato in invitado:
			if str(dato.FK_Reunion_id) == str(reunion_id):

				asunto = dato.FK_Reunion.FK_Comision.nombreComision
				mensaje = "Por medio de la presente se les notifica que el dia: "+str(dato.FK_Reunion.fechaReunion)+\
							"a las: "+dato.FK_Reunion.horaReunion+", se realizara una reunión en "+dato.FK_Reunion.lugar+";" \
							"\n" \
							"\nCorreo Invitado: "+ dato.email + \
							"\n" \
							"Esperamos su Participación.\n" \

				mail = EmailMessage(asunto, mensaje, to=[dato.email])
				mail.send()

		#ENVIAR CORREO INTEGRANTES COMISION
		for int in integrantes:
				asunto = int.FK_Comision.nombreComision
				mensaje = "Por medio de la presente se les notifica que el dia: "+str(reunion.fechaReunion)+\
							"a las: "+reunion.horaReunion+", se realizara una reunión en "+reunion.lugar+";" \
							"\n" \
							"\nCorreo Invitado: "+ int.FK_User.email + \
							"\n" \
							"Esperamos su Participación.\n" \

				mail = EmailMessage(asunto, mensaje, to=[int.FK_User.email])
				mail.send()

		return redirect('../../', reunion_id)
	return render(request, 'comision/reunionEnviar.html', {'reunion':reunion , 'temas':tema , 'archivos':archivo , 'invitados':invitado , 'reuniones':reuniones})

#------------------------ ACORDEMOS ------------------------
def acordemos(request, reunion_id):
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	integrante = Integrante.objects.all()
	acuerdo = Acuerdo.objects.all()
	asistente = Asistencia.objects.all()
	comision = Comision.objects.all()
	tema = Tema.objects.all()
	votaciones = Votacion.objects.all()

	participantes = 0;
	numAsistentes = 0;

	for cta , a in enumerate(asistente):
		if cta>0:
			numAsistentes = Asistencia.objects.filter(asiste = "Si" ,FK_Reunion_id = reunion_id)
			for count ,asis in enumerate(numAsistentes, 1):
				participantes = count;


	contexto = {'reunion':reunion, 'temas':tema, 'integrantes':integrante, 'comisiones':comision,'asistente':asistente,
				'acuerdo':acuerdo,'participantes':participantes,'votaciones':votaciones,'numAsistentes':numAsistentes,
				}
	return render(request, 'comision/Acordemos.html', contexto)


#GENERAR ACTA EN FORMATO PDF
from django.http import HttpResponse
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def pdf(request, reunion_id):
	reunion = get_object_or_404(Reunion, pk=reunion_id)

	#datos de la Comisión
	comisionID= reunion.FK_Comision_id
	nombreComision=reunion.FK_Comision.nombreComision
	LugarReunion=reunion.lugar
	horaReunion=reunion.horaReunion
	fechaReunion=reunion.fechaReunion
	fecha_str = datetime.strftime(fechaReunion, '%d/%m/%Y')

	#Miembros de la Comisión
	miembros=Integrante.objects.all()

	#Asistentes a la Reunión
	asistentes = Asistencia.objects.filter(FK_Reunion_id = reunion_id)

	#invitados a la reunion
	invitadoReunion= Invitado.objects.filter(FK_Reunion_id = reunion_id)

	#Temas de la Reunión
	temasReunion = Tema.objects.filter(FK_Reunion_id = reunion.id)

	acuerdos = Acuerdo.objects.all()


	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename='+nombreComision+'/'+fecha_str+'.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)

	#Título
	c.setLineWidth(.3)

	c.setFont('Helvetica-Bold',16)
	c.drawString(30,750,"Comision: "+ nombreComision)
	

	c.setFont('Helvetica',14)
	c.drawString(30,730,"Lugar: "+ LugarReunion)

	c.setFont('Helvetica',12)
	c.drawString(30,710,"Hora: "+ horaReunion)

	c.setFont('Helvetica',12)
	c.drawString(100,710,"Fecha: "+ fecha_str)

	#linea de separación
	c.line(30,700,560,700)

	#Datos Universidad
	c.setFont('Helvetica',12)
	c.drawString(410,750,"Universidad de Playa Ancha")
	c.setFont('Helvetica',12)
	c.drawString(425,735,"Facultad de Ingenieria")
	#c.line(440,738,560,738)

	#titulo
	c.setFont('Helvetica-Bold',18)
	c.drawString(200,670,"Información de la Reunión")

	#linea de separación
	c.line(30,650,560,650)

	#izquierda Miembros de la Comisión
	c.setFont('Helvetica-Bold',13)
	c.drawString(50,630,"Miembros Comisión:")
	altoMiembros = 615
	for miembro in miembros:
		if miembro.FK_Comision_id == comisionID:
			c.setFont('Helvetica',12)
			c.drawString(50,altoMiembros,miembro.FK_User.first_name+" "+miembro.FK_User.last_name)
			altoMiembros=altoMiembros-15

	#derecha
	c.setFont('Helvetica-Bold',13)
	c.drawString(330,630,"Asistencia Reunión:")
	altoAsistente = 615
	for asistente in asistentes:
		if asistente.asiste == "Si":
			c.setFont('Helvetica',12)
			c.drawString(330,altoAsistente,"Presente - "+asistente.FK_Integrante.FK_User.first_name+" "+asistente.FK_Integrante.FK_User.last_name)
			altoAsistente=altoAsistente-15
		else:
			c.setFont('Helvetica',12)
			c.drawString(330,altoAsistente,"Ausente - "+asistente.FK_Integrante.FK_User.first_name+" "+asistente.FK_Integrante.FK_User.last_name)
			altoAsistente=altoAsistente-15

	#izquierda
	c.setFont('Helvetica-Bold',13)
	c.drawString(50,520,"Temas:")
	altoTemas=505
	for tema in temasReunion:
		c.setFont('Helvetica',12)
		c.drawString(50,altoTemas,"- "+tema.tema)
		altoTemas=altoTemas-15


	#derecha
	c.setFont('Helvetica-Bold',13)
	c.drawString(340,520,"Invitados Comisión:")
	altoTemas=505
	for invitado in invitadoReunion:
		c.setFont('Helvetica',12)
		c.drawString(340,altoTemas,"- "+invitado.nombre+" "+invitado.apellido)
		altoTemas=altoTemas-15


	#linea de separación
	c.line(30,460,560,460)

	#linea de separación
	c.line(30,420,560,420)

	#Acuerdos
	c.setFont('Helvetica-Bold',18)
	c.drawString(260,435,"Acuerdos:")
	altoAcuerdo=400
	for tema in temasReunion:
		for acuerdo in acuerdos:
			if tema.id == acuerdo.FK_Tema_id:
				c.setFont('Helvetica',14)
				c.drawString(140,altoAcuerdo,"- "+acuerdo.FK_Tema.tema+": "+acuerdo.acuerdo+"||"+acuerdo.estado)
				altoAcuerdo=altoAcuerdo-20


	c.save()
	pdf=buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response



#	EDITAR ACUERDO
def acuerdo_editar(request,reunion_id, acuerdo_id ):
	acuerdoEstado = get_object_or_404(Acuerdo, pk = acuerdo_id)
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	if request.method == 'GET':
		form = acuerdoEstadoForm(instance=acuerdoEstado)
	else:
		form = acuerdoEstadoForm(request.POST, instance=acuerdoEstado)
		if form.is_valid():
			form.save()
		return redirect('../../../'+reunion_id)
	return render(request, 'comision/acuerdoEditar.html', {'form':form,'reunion':reunion,'acuerdoEstado':acuerdoEstado})


#	ACORDEMOS
def acuerdo_crear(request, tema_id, reunion_id):
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	tema = get_object_or_404(Tema, pk = tema_id)
	if request.method == 'POST':
		form = AcuerdoForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.FK_Tema_id = tema.id
			post.save()
			form.save()
		return redirect('../../../'+reunion_id)
	else:
		form = AcuerdoForm()
		args = {'form':form ,'tema':tema,'reunion':reunion}
	return render(request, 'comision/acuerdo_form.html', args)






# COMENTARIO
def comentarios(request, acuerdo_id, asistencia_id, reunion_id):
	acuerdo = get_object_or_404(Acuerdo, pk = acuerdo_id)
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	asistencia = get_object_or_404(Asistencia, pk = asistencia_id)
	if request.method == 'POST':
		form = ComentarioForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.FK_Acuerdo_id = acuerdo.id
			post.FK_Asistencia_id = asistencia.id
			form.save()
		return redirect('../../../../'+reunion_id)
	else:
		form = ComentarioForm()
		args = {'form':form ,'acuerdo':acuerdo,'asistencia':asistencia,'reunion':reunion}
	return render(request, 'comision/comentario_form.html', args)

# VOTACION
def votacion(request, acuerdo_id, asistencia_id, reunion_id):
	acuerdo = get_object_or_404(Acuerdo, pk = acuerdo_id)
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	asistencia = get_object_or_404(Asistencia, pk = asistencia_id)
	if request.method == 'POST':
		form2 = AcuerdoForm(request.GET, instance=acuerdo)
		form = VotacionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.FK_Acuerdo_id = acuerdo.id
			post.FK_Asistencia_id = asistencia.id
			form.save()
		return redirect('../../../../'+reunion_id)
	else:
		form = VotacionForm()
		args = {'form':form ,'acuerdo':acuerdo,'asistencia':asistencia,'reunion':reunion}
	return render(request, 'comision/votacion_form.html', args)


# ACUERDO LISTA
def listaAcuerdos(request):
	votacion = Votacion.objects.all()
	archivo = Archivo.objects.all()
	datosArchivo = Tema.objects.all()
	acuerdo = Acuerdo.objects.all()
	acuerdoAceptados = Acuerdo.objects.filter(estado="Aceptado")
	acta = Acta.objects.all()
	integrantes=Integrante.objects.all()


	contexto = {'integrantes':integrantes,'acta':acta,'archivo':datosArchivo,'acuerdos':acuerdo,'votaciones':votacion,'archivos':archivo,'acuerdoAceptados':acuerdoAceptados}
	return render(request, 'acuerdos.html', contexto)

#------------------------SESION------------------------
def salir(request):
    logout(request)
    return redirect('/')

#INFORMACION PARA "MENU" DE CADA USUARIO
def infoBase(request):
	datos1 = Integrante.objects.all()
	contexto = {'integrante':datos1 }
	return render(request, 'base.html', contexto)
