from django.views.generic.edit import CreateView
from .models import Cartao, Pix
from django.urls import reverse_lazy


class CartaoCreate(CreateView):
    model = Cartao
    fields = ['nome', 'email','cpf','numeroCartao','mes','ano','cvv']
    template_name = 'cadastros/cartao.html'
    success_url = reverse_lazy('inicio')

class PixCreate(CreateView):
        model = Pix
        fields = ['nome', 'email','cpf']
        template_name = 'cadastros/pix1.html'
        success_url = reverse_lazy('pix2')

   