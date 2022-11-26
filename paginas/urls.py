from django.urls import path
from .views import PaginaInicial, Pagamento, Pix




urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('pagamento/', Pagamento.as_view(), name='pagamento'),
    path('pix2/', Pix.as_view(), name='pix2'),
]



