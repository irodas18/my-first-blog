from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Examen, Tecnico
from django.utils.dateparse import parse_date

def nuevo_registro(request):
    if request.method == 'POST':
        # Procesar el formulario aquí
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        tecnico_id = request.POST.get('tecnico')
        examen_id = request.POST.get('examen')
        monto = request.POST.get('monto')
        tipo_consulta = request.POST.get('tipo_consulta')

        # Lógica para guardar el registro en la base de datos
        # ...

        return redirect('nuevo_registro')  # Redirige a la misma página o a otra página de éxito

    tecnicos = Tecnico.objects.all()
    examenes = Examen.objects.all()
    return render(request, 'gestion_examenes/nuevo_registro.html', {'tecnicos': tecnicos, 'examenes': examenes})

def generar_reporte(request):
    if request.method == 'GET':
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')

        # Lógica para generar el reporte
        # ...

        total_recaudado = 0  # Calcula el total recaudado
        return render(request, 'gestion_examenes/generar_reporte.html', {
            'total_recaudado': total_recaudado,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
        })
