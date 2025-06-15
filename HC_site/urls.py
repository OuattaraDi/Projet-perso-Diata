from django.urls import path
from . import views
from .views import page_detail

urlpatterns = [

    path('', views.accueil, name='accueil'),
    path('<slug:slug>/', page_detail, name='page_detail'),
    path('prendre-rdv/', views.prendre_rdv, name='prendre_rdv'),
    path('merci/', views.merci, name='merci'), # si tu as une page de remerciement
    path('inscription-coiffeuse-reussie/', views.page_detail, {'slug': 'inscription-coiffeuse-reussie'}, name='inscription_coiffeuse_reussie'),

   

]

