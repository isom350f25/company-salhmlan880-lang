from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth=models.DateField()
    position=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=8)
    joined_on=models.DateField()
    
    def __str__(self):
        return f"{self.name}- {self.position}"