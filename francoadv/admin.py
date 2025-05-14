from django.contrib import admin
from francoadv.models import PaginaInicio, PaginaSobre, PaginaServicos, ComponenteInsta, ComponenteContato, ComponenteCTA

class PaginaInicioAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class PaginaSobreAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class PaginaServicosAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class ComponenteInstaAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class ComponenteContatoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class ComponenteCTAAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

admin.site.register(PaginaInicio, PaginaInicioAdmin)
admin.site.register(PaginaSobre, PaginaSobreAdmin)
admin.site.register(PaginaServicos, PaginaServicosAdmin)
admin.site.register(ComponenteInsta, ComponenteInstaAdmin)
admin.site.register(ComponenteContato, ComponenteContatoAdmin)
admin.site.register(ComponenteCTA, ComponenteCTAAdmin)
