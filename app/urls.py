from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('sobre/', views.sobre, name="sobre"),
    path('clubes/', views.clubes, name="clubes"),
    path('editoras/', views.editoras, name="editoras"),
    path('livros/', views.livros, name="livros"),
    path('configuracoes/', views.configuracoes, name="configuracoes"),
]
