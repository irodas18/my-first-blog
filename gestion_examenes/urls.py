from django.urls import path
from . import views

urlpatterns = [
    path('nuevo-registro/', views.nuevo_registro, name='nuevo_registro'),
    path('generar-reporte/', views.generar_reporte, name='generar_reporte'),
]
