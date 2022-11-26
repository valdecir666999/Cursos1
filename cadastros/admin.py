from django.contrib import admin

# Importar as classes
from .models import Cartao, Pix


# Register yours models here.
# python manage.py makemirations Atualizar banco de dados
# python manage.py migrate Executar e criar banco de dados


admin.site.register(Cartao)
admin.site.register(Pix)
