from django.contrib import admin
from personal.models import Produtos, Carrosel

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('produto_name', 'descricao', 'status', 'data_insercao')
    search_fields = ('produto_name', 'descricao')
admin.site.register(Produtos, ProdutosAdmin)

class CarroselAdmin(admin.ModelAdmin):
    search_fields = ('imagem_name', )
admin.site.register(Carrosel, CarroselAdmin)