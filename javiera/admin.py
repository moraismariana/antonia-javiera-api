from django.contrib import admin
from javiera.models import Artigo, PaginaInicio, PaginaSobre, ComponenteContato

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class PaginaInicioAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class PaginaSobreAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class ComponenteContatoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(PaginaInicio, PaginaInicioAdmin)
admin.site.register(PaginaSobre, PaginaSobreAdmin)
admin.site.register(ComponenteContato, ComponenteContatoAdmin)