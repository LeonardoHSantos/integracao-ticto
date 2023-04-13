from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("Venda-Realizada/", views.Venda_Realizada, name="Venda_Realizada"),
    path("Venda-Recusada/", views.Venda_Recusada, name="Venda_Recusada"),
    path("Chargeback/", views.Chargeback, name="Chargeback"),
    path("Reembolso/", views.Reembolso, name="Reembolso"),
    path("Encerrado/", views.Encerrado, name="Encerrado"),
    path("Assinatura-Cancelada/", views.Assinatura_Cancelada, name="Assinatura_Cancelada"),
    path("Tempo-de-Teste/", views.Tempo_de_Teste, name="Tempo_de_Teste"),
]
# Abandono de Carrinho
# Tempo de Teste
# Aguardando Pagamento
# Encerrado
# Pix Expirado
# Assinatura Cancelada
# Pix Gerado
# Boleto Atrasado
# Reembolso
# Boleto Impresso
# Venda Realizada
# Chargeback
# Venda Recusada