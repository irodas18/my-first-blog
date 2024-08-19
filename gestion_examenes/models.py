from django.db import models

class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Examen(models.Model):
    nombre_examen = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_examen

class Registro(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_consulta = models.CharField(max_length=15, choices=[('hospitalización', 'Hospitalización'), ('consulta', 'Consulta')])

    def __str__(self):
        return f"{self.fecha} - {self.tecnico} - {self.examen}"

class Reporte(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    total_recaudado = models.DecimalField(max_digits=10, decimal_places=2)