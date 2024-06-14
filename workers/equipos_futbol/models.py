from django.db import models

# Create your models here.
class EquipoFutbol(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    equipo = models.CharField(max_length=100,blank=True,default='')

    class Meta:
        db_table = 'equipos_de_futbol'
