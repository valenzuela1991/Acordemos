# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import ConvocatoriaForm, AcuerdoForm, InvitadosForm,  TemaForm , AsistenciaForm, ComentarioForm ,ArchivoForm, EnlaceForm, VotacionForm
from .models import Reunion, Integrante, Acuerdo, Tema, Comision, Asistencia, Votacion,Archivo ,Invitado
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
	comision = Comision.objects.all()
	return render(request, 'comision/comentarioVotacion.html',{'reu':reu,'reuniones':reunion,'temas':tema,'asistente':asistente,'acuerdo':acuerdo,'integrantes':integrante})


#	ASISTENCIA
#def pasarAsistencia(request, reunion_id):
	#reu = get_object_or_404(Reunion, pk = reunion_id)
	#integrante = Integrante.objects.filter(FK_Comision_id = reu.FK_Comision_id)
	#invitado = Invitado.objects.filter(FK_Reunion_id = reunion_id)
	#return render(request, 'comision/asistencia_form.html', {'reu':reu,'integrante':integrante,'invitado':invitado})



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


#-------------------------------------------------------------
#------------------------MIS REUNIONES------------------------
from .models import Enlace, Archivo
#	LISTAR REUNIONES
def reunion_list(request):
	inv = Invitado.objects.all()
	integrante = Integrante.objects.all()
	archivo = Archivo.objects.all()
	reunion = Reunion.objects.all().order_by('id')
	comision = Comision.objects.all()
	tema = Tema.objects.all()
	enlace = Enlace.objects.all()
	contexto = {'inv':inv,'reuniones':reunion, 'temas':tema, 'integrantes':integrante, 'comisiones':comision,'enlaces':enlace,'archivos':archivo}
	return render(request, 'comision/reunion_lista.html', contexto)

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
	invitado = get_object_or_404(Invitado, pk= invitado_id)
	if request.method == 'POST':
		invitado.delete()
		return redirect('../../../', invitado_id)
	return render(request, 'comision/invitado_delete.html', {'invitado':invitado})

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
	archivo = Archivo.objects.all()
	invitado = Invitado.objects.all()
	integrante = Integrante.objects.all()
	tema = Tema.objects.all()
	reuniones = Reunion.objects.all()


	if request.method == 'POST':
		#ENVIAR CORREO INVITADOS
		for dato in invitado:
			if str(dato.FK_Reunion_id) == str(reunion_id):

				asunto = dato.FK_Reunion.FK_Comision.nombreComision
				mensaje = "Por medio de la presente se les notifica que el dia: "+str(dato.FK_Reunion.fechaReunion)+\
							"a las: "+dato.FK_Reunion.horaReunion+", se realizara una reunión en "+dato.FK_Reunion.lugar+";" \
							"el motivo de dicha reunión es para tratar temas como :  " \
							"\n" \
							"\nCorreo Invitado: "+ dato.email + \
							"\n" \
							"Esperamos su Participación.\n" \
							#"LINK PARA COMPROBAR PARTICIPACION"

				mail = EmailMessage(asunto, mensaje, to=[dato.email])
				mail.send()

		return redirect('../../', reunion_id)
	return render(request, 'comision/reunionEnviar.html', {'reunion':reunion , 'temas':tema , 'archivos':archivo , 'invitados':invitado , 'reuniones':reuniones})


#-----------------------------------------------------------
#------------------------ ACORDEMOS ------------------------

cta = 0;

def acordemos(request, reunion_id):
	reunion = get_object_or_404(Reunion, pk = reunion_id)
	integrante = Integrante.objects.all()
	acuerdo = Acuerdo.objects.all()
	asistente = Asistencia.objects.all()
	comision = Comision.objects.all()
	tema = Tema.objects.all()

	quorum = reunion.FK_Comision.quorum

	for contar in asistente:
		if contar.asiste == "Si":
			for count , a in enumerate(contar):
				participantes = count ;


	contexto = {'reunion':reunion, 'temas':tema, 'integrantes':integrante, 'comisiones':comision,'asistente':asistente,'acuerdo':acuerdo,'participantes':participantes}
	return render(request, 'comision/Acordemos.html', contexto)


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
def comentarios(request, acuerdo_id, asistencia_id):
	acuerdo = get_object_or_404(Acuerdo, pk = acuerdo_id)
	asistencia = get_object_or_404(Asistencia, pk = asistencia_id)
	if request.method == 'POST':
		form = ComentarioForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.FK_Acuerdo_id = acuerdo.id
			post.FK_Asistencia_id = asistencia.id
			form.save()
		return redirect('../../../')
	else:
		form = ComentarioForm()
		args = {'form':form ,'acuerdo':acuerdo,'asistencia':asistencia}
	return render(request, 'comision/comentario_form.html', args)

# VOTACION
def votacion(request, acuerdo_id, asistencia_id):
	acuerdo = get_object_or_404(Acuerdo, pk = acuerdo_id)
	asistencia = get_object_or_404(Asistencia, pk = asistencia_id)
	if request.method == 'POST':
		form = VotacionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.FK_Acuerdo_id = acuerdo.id
			post.FK_Asistencia_id = asistencia.id
			form.save()
		return redirect('../../../')
	else:
		form = VotacionForm()
		args = {'form':form ,'acuerdo':acuerdo,'asistencia':asistencia}
	return render(request, 'comision/votacion_form.html', args)


# ACUERDO LISTA
def listaAcuerdos(request):
	dato = Votacion.objects.all()
	dato2 = Archivo.objects.all()
	datosArchivo = Tema.objects.all()
	datosAcuerdo = Acuerdo.objects.all()
	contexto = {'archivo':datosArchivo,'acuerdo':datosAcuerdo,'datos':dato,'datos2':dato2}
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
