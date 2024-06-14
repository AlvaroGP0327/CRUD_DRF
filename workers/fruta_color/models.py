from django.db import models

# Create your models here.

# Create your models here.
class FrutaColor(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    fruta = models.CharField(max_length=100,blank=True,default='')
    color = models.CharField(max_length=100,blank=True,default='')

    class Meta:

        db_table = 'Fruta y Color'
