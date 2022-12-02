from django.contrib import admin
from .models import Cliente, Login, Produto, Frete, Compra


class ProdutoAdmin(admin.ModelAdmin):
    model = Produto

    list_display = ('nomeprod', 'quantidadedisp', 'valor')

admin.site.register(Cliente)
admin.site.register(Login)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Frete)
admin.site.register(Compra)