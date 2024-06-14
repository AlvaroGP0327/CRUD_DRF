from django.db import models

# Create your models here.
class Capitales(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    country = models.CharField(max_length=100,blank=True,default='')
    capital = models.CharField(max_length=100,blank=True,default='')

    class Meta:

        db_table = 'PaisesyCapitales'