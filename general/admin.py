from django.contrib import admin

from general.models import TrabajadorModel

# Register your models here.


class TrabajadorModelAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre',)
    search_fields = ('matricula', 'nombre', )
    list_per_page = 500

admin.site.register(TrabajadorModel, TrabajadorModelAdmin)