# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from Apps.Acordemos.models import *

#Administrador
admin.site.register(TipoUnidad)
admin.site.register(Unidad)
admin.site.register(TipoDocumentoLegal)
admin.site.register(DocumentoLegal)
admin.site.register(Comision)
admin.site.register(TipoComision)
admin.site.register(Documento_TipoComision)
admin.site.register(TipoRol)
admin.site.register(Integrante)

#Crear Convocatoria
admin.site.register(Invitado)
admin.site.register(Reunion)
admin.site.register(Tema)
admin.site.register(Archivo)
admin.site.register(Enlace)

#ACORDEMOS
admin.site.register(Asistencia)
admin.site.register(Votacion)
admin.site.register(Comentario)
admin.site.register(Acuerdo)