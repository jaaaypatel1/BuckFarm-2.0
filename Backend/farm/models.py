from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    zip  = models.DecimalField(max_digits=5)    
    dateHarvested = models.DecimalField(max_digits=10)
    businessName = models.TextField()
    
    def __str__(self):
        return self.name