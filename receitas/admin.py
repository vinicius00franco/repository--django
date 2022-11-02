from django.contrib import admin
from .models import Receita
#import models receita


# Register your models here.

#registrando o modelo de receitas no admin
#criando o rote do modelo de receitas para admin

admin.site.register(Receita)