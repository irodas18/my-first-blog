from django.shortcuts import render
from .forms import RegistroForm

def nuevo_registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')  # Ajusta la redirección según sea necesario
    else:
        form = RegistroForm()
    return render(request, 'gestion_examenes/nuevo_registro.html', {'form': form})