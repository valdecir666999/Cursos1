from django.views.generic import TemplateView


#Create your views here
class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

class Pix(TemplateView):
    template_name = 'paginas/pix2.html'



class Pagamento(TemplateView):
    template_name = 'paginas/pagamento.html'





