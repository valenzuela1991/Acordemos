from django import forms
from .models import Reunion, Acuerdo, Invitado,  Tema, Asistencia, Comentario, Votacion, Archivo,Enlace,Acta
from django.contrib.admin import widgets
#FORMULARIO DE CREAR CONVOCATORIA
class ConvocatoriaForm(forms.ModelForm):
	class Meta:
		model = Reunion

		fields = [
			#FK_Comision,
			'fechaReunion',
			'horaReunion',
			'lugar',
			#'FK_Invitado',
		]
		labels = {
			'fechaReunion': '1) Fecha en que se realizará la Reunión.',
			'horaReunion': '2) Hora de la Reunión.',
			'lugar': '3) Lugar de la Reunión.',
			#'FK_Invitado': 'Lista con todos los invitados registrados desde su Sesión.',
		}
		widgets = {
			'fechaReunion':forms.SelectDateWidget(attrs={'class':'form-control'}),
			'horaReunion':forms.TextInput(attrs={'class':'form-control'}),
			'lugar':forms.TextInput(attrs={'class':'form-control'}),
			#'FK_Invitado': forms.CheckboxSelectMultiple(),
		}

#FORMULARIO DE CREAR INVITADO
class InvitadosForm(forms.ModelForm):
	class Meta:
		model = Invitado

		fields = [
			'nombre',
			'apellido',
			'email',
		]
		labels = {
			'nombre': '1) Nombre.',
			'apellido': '2) Apellido.',
			'email': '3) Email.',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellido':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
		}

#FORMULARIO DE CREAR TEMA
class TemaForm(forms.ModelForm):
	class Meta:
		model = Tema

		fields = [
			#'FK_Reunion
			'tema',
		]
		labels = {
			'tema': 'Tema a tratar.',
		}
		widgets = {
			'tema':forms.TextInput(attrs={'class':'form-control'}),
		}

#FORMULARIO ARCHIVO
class ArchivoForm(forms.ModelForm):
	class Meta:
		model = Archivo

		fields = [
			#"FK_Tema",
			'media',
			'descripcion',
		]
		labels = {
			'media': '1) Selecciona un archivo.',
			'descripcion': '2) Descripción.',
		}
		widgets = {
			'descripcion':forms.Textarea(attrs={'class':'form-control'}),
		}


#FORMULARIO Acta
class ActaForm(forms.ModelForm):
	class Meta:
		model = Acta

		fields = [
			'media',
		]
		labels = {
			'media': 'Selecciona el Acta.',
		}


#FORMULARIO ENLACE
class EnlaceForm(forms.ModelForm):
	class Meta:
		model = Enlace

		fields = [
			#'FK_Tema',
			'url',
			'descripcion',
		]
		labels = {
			#'FK_Reunion': '1) Tema.',
			'url': '1) URL.',
			'descripcion': '2) Descripción.',
		}
		widgets = {
			#'FK_Tema':forms.Select(attrs={'class':'form-control'}),
			'url':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.Textarea(attrs={'class':'form-control'}),
		}


#FORMULARIO DE ASISTENCIA
class AsistenciaForm(forms.ModelForm):
	class Meta:
		model = Asistencia

		fields = [
			'asiste',
			'justificacion',
			'observacion',
		]
		labels = {
			'asiste': 'Presente.',
			'justificacion': 'Justificacion de los Ausentes.',
			'observacion': 'Observaciones.',
		}
		widgets = {
			'asiste': forms.Select(attrs={'class': 'form-control'}),
			'justificacion':forms.Textarea(attrs={'class':'form-control'}),
			'observacion':forms.Textarea(attrs={'class':'form-control'}),
		}

class acuerdoEstadoForm(forms.ModelForm):
	class Meta:
		model = Acuerdo

		fields = [
			#'FK_Tema',
			'estado',
			#'acuerdo',
		]
		labels = {
			'estado': 'Eliga el estado del Acuerdo.',
		}
		widgets = {
			'estado': forms.Select(attrs={'class': 'form-control'}),
		}


#FORMULARIO DE ACUERDO
class AcuerdoForm(forms.ModelForm):

	class Meta:
		model = Acuerdo

		fields = [
			#'FK_Tema',
			#'estado',
			'acuerdo',
		]
		labels = {
			#'FK_Tema': 'Tema a tratar',
			#'estado': 'Estado',
			'acuerdo': 'Acuerdo',
		}
		widgets = {
			#'FK_Tema':forms.Select(attrs={'class':'form-control'}),
			#'estado': forms.Select(attrs={'class':'form-control'}),
			'acuerdo': forms.Textarea(attrs={'class':'form-control'}),
		}


#FORMULARIO DE COMENTARIO

class ComentarioForm(forms.ModelForm):

	class Meta:
		model = Comentario

		fields = [
			'comentario',
		]
		labels = {
			'comentario': 'Comentario.',
		}
		widgets = {
			'comentario':forms.Textarea(attrs={'class':'form-control'}),
		}

#FORMULARIO DE VOTACION

class VotacionForm(forms.ModelForm):

	class Meta:
		model = Votacion

		fields = [
			'voto',
		]
		labels = {
			'voto': 'Voto.',
		}
		widgets = {
			'voto':forms.Select(attrs={'class':'form-control'}),
		}