from django.urls import path
from .views import CartaoCreate, PixCreate



urlpatterns = [ 
  path('cadastrar/cartao', CartaoCreate.as_view(), name='cadastrar-cartao'),
  path('pix1', PixCreate.as_view(), name='pix1'),
]



