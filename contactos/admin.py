from django.contrib import admin

from .models import Contacto, Empresa


class EmpresaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('denominacion',
                       'n_comercial',
                       'calle',
                       'nif',
                       )
        }),
        ('Dirección', {
            'classes': ('collapse',),
            'fields': ('calle2',
                       'ciudad',
                       'provincia',
                       'cp',
                       'pais',
                       'email',
                       'tfno',
                       'movil'),
        }),
    )
    resource_class = Empresa
    search_fields = ('denominacion', 'n_comercial')
    list_display = ('denominacion',
                    'n_comercial',
                    'nif',
                    'provincia',
                    )
    list_display_links = ('n_comercial',
                          'nif',
                          'provincia')




class ContactoAdmin(admin.ModelAdmin):
    search_fields = ('empresa', 'nombre')
    list_display = ('nombre',
                    'empresa',
                    'email',
                    'tfno',
                    )
    list_display_links = ('nombre',
                          'empresa',
                          )


admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Contacto, ContactoAdmin)
