from django.urls import path
from . import views
urlpatterns = [
    path('cadastrar_diarista', views.cadastrar_diarista, name="cadastrar_diarista"),
    path('listar_diarista', views.listar_diarista, name="listar_diarista"),
]
