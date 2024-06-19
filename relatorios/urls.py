from django.urls import path
from .views import AbastecimentoRelatorioPDFView

urlpatterns = [
    path('relatorio/', AbastecimentoRelatorioPDFView.as_view(), name='abastecimento-relatorio'),
]
