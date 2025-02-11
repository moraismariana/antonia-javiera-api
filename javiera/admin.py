from django.contrib import admin
from javiera.models import Artigo


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

admin.site.register(Artigo, ArtigoAdmin)