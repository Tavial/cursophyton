from django.contrib import admin
from anuncios.models import Anuncio, Tipo, Categoria, Usuario

# Register your models here.

class AnuncioAdmin(admin.ModelAdmin):
    list_display=("fecha","titulo","descripcion")
    search_fields=("titulo","descripcion","fecha")
    list_filter = ("categoria","tipo","usuario")


admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Tipo)
admin.site.register(Categoria)
admin.site.register(Usuario)
