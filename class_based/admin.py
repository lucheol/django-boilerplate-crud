from django.contrib import admin
from .models import Estado
# Register your models here.


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    '''Admin View for Estado'''

    list_display = ('NomeEstado', 'Sigla')
