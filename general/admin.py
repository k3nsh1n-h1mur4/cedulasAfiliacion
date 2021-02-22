from django.contrib import admin

from general.models import TrabajadorModel

# Register your models here.


class TrabajadorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'matricula', 'nombre',)
    search_fields = ('id', 'matricula', 'nombre', )
    list_per_page = 500

admin.site.register(TrabajadorModel, TrabajadorModelAdmin)