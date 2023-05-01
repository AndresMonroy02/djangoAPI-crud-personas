from django.db import models

# Create your models here.
class Personas(models.Model):
    id = models.AutoField(primary_key=True)
    nombres =  models.CharField(max_length=255)
    apellidos =  models.CharField(max_length=255)
    programa =  models.CharField(max_length=255)

    def __str__(self):
        return self.nombres