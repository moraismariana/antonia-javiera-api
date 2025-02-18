from django.contrib import admin
from javiera.models import Artigo, InicioTexto, InicioImg, InicioBg, SobreTexto, SobreImg, ComponenteArtigosTexto, ComponenteContatoTexto

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class InicioTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class InicioImgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class InicioBgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class SobreTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class SobreImgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class ComponenteArtigosTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class ComponenteContatoTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(InicioTexto, InicioTextoAdmin)
admin.site.register(InicioImg, InicioImgAdmin)
admin.site.register(InicioBg, InicioBgAdmin)
admin.site.register(SobreTexto, SobreTextoAdmin)
admin.site.register(SobreImg, SobreImgAdmin)
admin.site.register(ComponenteArtigosTexto, ComponenteArtigosTextoAdmin)
admin.site.register(ComponenteContatoTexto, ComponenteContatoTextoAdmin)