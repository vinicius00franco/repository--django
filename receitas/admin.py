from django.contrib import admin
from .models import Receita, Pessoa
#import models receita


# Register your models here.



class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id','nome_receita','categoria', 'tempo_preparo')
    list_display_links = ('id','nome_receita')
    search_fields = ('no_receita',)
    list_filter = ('categoria',) #filtro por categoria
    list_per_page: 5


#registrando o modelo de receitas no admin
#criando o rote do modelo de receitas para admin

#registrando display de receitas
admin.site.register(Receita, ListandoReceitas)

admin.site.register(Pessoa)