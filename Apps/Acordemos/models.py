# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

#----------------CAMPOS QUE LLENA EL ADMINISTRADOR-----------------------
class TipoUnidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre+"."

#Vicerrectoria, Rectoria, Secretaria General,
# Comite, Programa Postgrado, Carrera, Facultad

class Unidad(models.Model):
    id = models.AutoField(primary_key=True)
    FK_TipoUnidad = models.ForeignKey(TipoUnidad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre+"."

#Facultad de Ingenieria

class TipoDocumentoLegal(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30)
    def __str__(self):
        return self.tipo+"."

#Circular, Resolucion, Decreto, Decreto Exento

class DocumentoLegal(models.Model):
    id = models.AutoField(primary_key=True)
    num = models.IntegerField()
    ano = models.IntegerField()
    #tipo = models.CharField(max_length=30)
    referencia = models.CharField(max_length=30)
    #Text referencia
    enlace = models.CharField(max_length=50)
    FK_TipoDocumentoLegal = models.ForeignKey(TipoDocumentoLegal, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.num)+"-Tipo: "+str(self.FK_TipoDocumentoLegal)

class Comision(models.Model):
    id = models.AutoField(primary_key=True)
    nombreComision = models.CharField(max_length=100)
    descripcion = models.TextField()
    numeroIntegrante = models.IntegerField()
    SI = 'Si'
    NO = 'No'
    activa_opciones = (
        (SI, 'SI'),
        (NO, 'NO'),
    )
    activa = models.CharField(
        max_length=2,
        choices=activa_opciones,
        default=SI,
    )
    FK_DocumentoLegal = models.ForeignKey(DocumentoLegal, on_delete=models.CASCADE)
    FK_Unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    quorum = models.IntegerField()
    def __str__(self):
        return self.nombreComision+"."

class TipoComision(models.Model):
    id = models.AutoField(primary_key=True)
    nombreComision = models.CharField(max_length=100)
    quorum = models.IntegerField()
    descripcion = models.TextField()
    numeroIntegrante = models.IntegerField()
    def __str__(self):
        return self.nombreComision+"."

class Documento_TipoComision(models.Model):
    id = models.AutoField(primary_key=True)
    FK_DocumentoLegal = models.ForeignKey(DocumentoLegal, on_delete=models.CASCADE)
    TipoComision = models.ForeignKey(TipoComision, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.TipoComision)+"-"+str(self.FK_DocumentoLegal)

class TipoRol(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=10)
    def __str__(self):
        return str(self.rol)

#Secretario, Presidente, Integrante

class Integrante(models.Model):
    id = models.AutoField(primary_key=True)
    FK_User = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    FK_Comision = models.ForeignKey(Comision, on_delete=models.CASCADE)
    FK_TipoRol = models.ForeignKey(TipoRol, on_delete=models.CASCADE)
    SI = 'Si'
    NO = 'No'
    vota_opciones = (
        (SI, 'SI'),
        (NO, 'NO'),
    )
    vota = models.CharField(
        max_length=2,
        choices=vota_opciones,
        default=SI,
    )
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    def __str__(self):
        return str(self.FK_User.email)+"-"+str(self.FK_Comision)+"."

#----------------CAMPOS QUE LLENA SECRETARIO O PRESIDENTE-----------------------

#----------------CREAR CONVOCATORIA-----------------------

class Reunion(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Comision = models.ForeignKey(Comision, on_delete=models.CASCADE)
    fechaEnvio = models.DateTimeField(default=datetime.now, blank=True)
    fechaReunion = models.DateField()
    horaReunion = models.CharField(max_length=10)
    lugar = models.CharField(max_length=50)
    def __str__(self):
        return str(self.FK_Comision)+"#"+str(self.id)

class Invitado(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return self.email

class Tema(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    tema = models.CharField(max_length=40)
    def __str__(self):
        return str(self.tema)+"."

class Archivo(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    media = models.FileField()
    descripcion = models.TextField()
    def __str__(self):
        return str(self.media)+"."


class Enlace(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)
    descripcion = models.TextField()


#----------------ACORDEMOS-----------------------

#  Primero se pasa asisntencia de los participantes de la Reunion
class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE)
    FK_Reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    # Opciones de Asistencia
    SI = 'Si'
    NO = 'No'
    asiste_opciones = (
        (SI, 'SI'),
        (NO, 'NO'),
    )
    asiste = models.CharField(
        max_length=2,
        choices=asiste_opciones,
        default=SI,
    )
    justificacion = models.TextField(default="Justificación")
    observacion = models.TextField(default="Observación")
    def __str__(self):
        return str(self.FK_Integrante)


#   Segundo se generan Acuerdos por cada tema
class Acuerdo(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    acuerdo = models.TextField()
    #FK_Asistencia = models.ManyToManyField(Asistencia, blank=True)
    # Opciones de Estado
    PENDIENTE = 'Pendiente'
    ACEPTADO = 'Aceptado'
    RECHAZADO = 'Rechazado'
    estado_opciones = (
        (PENDIENTE, 'PENDIENTE'),
        (ACEPTADO, 'ACEPTADO'),
        (RECHAZADO, 'RECHAZADO'),
    )
    estado = models.CharField(
        max_length=10,
        choices=estado_opciones,
        default=PENDIENTE,
    )
    def __str__(self):
        return str(self.FK_Tema)+str(self.acuerdo)


##Acta
class Acta(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Acuerdo = models.ForeignKey(Acuerdo, on_delete=models.CASCADE)
    media = models.FileField()


#   Cada acuerdo puede tener un comentario  o mas
class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)
    FK_Acuerdo = models.ForeignKey(Acuerdo, on_delete=models.CASCADE)
    comentario = models.TextField()
    def __str__(self):
        return str(self.FK_Asistencia)+"--"+str(self.FK_Acuerdo)+"--Comentario: "+str(self.comentario)+"."

#   Finalmente los integrantes votan sobre el acuerdo.
class Votacion(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)
    FK_Acuerdo = models.ForeignKey(Acuerdo, on_delete=models.CASCADE)
    APRUEBA = 1
    NOAPRUEBA = -1
    ABSTIENE = 0
    voto_opciones = (
        (APRUEBA, "Aprueba"),
        (NOAPRUEBA, "No Aprueba"),
        (ABSTIENE, "Abstiene"),
    )
    voto = models.IntegerField(
        choices=voto_opciones,
        default=1,
    )
    def __str__(self):
        return str(self.voto)+"--Acuerdo: "+str(self.FK_Acuerdo)+"."

