from django.db import models


# Create your models here.
class ClassAnnotation(models.Model):
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.name
