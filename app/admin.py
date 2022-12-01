from django.contrib import admin
from .models import Cliente, Login, Produto, Frete, Compra

admin.site.register(Cliente)
admin.site.register(Login)
admin.site.register(Produto)
admin.site.register(Frete)
admin.site.register(Compra)