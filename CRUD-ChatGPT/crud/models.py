from django.db import models

class Exemplo(models.Model):
    campo1 = models.CharField(max_length=50)
    campo2 = models.IntegerField()
    campo3 = models.BooleanField()

