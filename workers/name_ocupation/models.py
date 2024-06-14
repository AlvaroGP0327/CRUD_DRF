from django.db import models

# Create your models here.
class Worker(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    name = models.CharField(max_length=100,blank=True,default='')
    ocupation = models.CharField(max_length=100,blank=True,default='')

    class Meta:

        db_table = 'Especialidad de los trabajadores'

    #hereda un metodo save() para guardar el objeto
        
class JobSite(models.Model):
    city = models.CharField(max_length=100,blank=True,default='')
    company = models.CharField(max_length=100,blank=True,default='')

    class Meta:
        db_table = 'Ubicacion y Compania'

