from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("Abandono-de-Carrinho/", views.Abandono_de_Carrinho, name="Abandono_de_Carrinho"),
    path("Tempo-de-Teste/", views.Tempo_de_Teste, name="Tempo_de_Teste"),
    path("Aguardando-Pagamento/", views.Aguardando_Pagamento, name="Aguardando_Pagamento"),
    path("Encerrado/", views.Encerrado, name="Encerrado"),
    path("Pix-Expirado/", views.Pix_Expirado, name="Pix_Expirado"),
    path("Assinatura-Cancelada/", views.Assinatura_Cancelada, name="Assinatura_Cancelada"),
    path("Pix-Gerado/", views.Pix_Gerado, name="Pix_Gerado"),
    path("Boleto-Atrasado/", views.Boleto_Atrasado, name="Boleto_Atrasado"),
    path("Reembolso/", views.Reembolso, name="Reembolso"),
    path("Boleto-Impresso/", views.Boleto_Impresso, name="Boleto_Impresso"),
    path("Venda-Realizada/", views.Venda_Realizada, name="Venda_Realizada"),
    path("Chargeback/", views.Chargeback, name="Chargeback"),
    path("Venda-Recusada/", views.Venda_Recusada, name="Venda_Recusada"),
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