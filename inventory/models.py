from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField()
    price= models.FloatField()
    discount=models.FloatField()
    product_date = models.DateField(auto_now_add=True)
    #product_image=models.CharField(max_length=500)
    image = models.ImageField(upload_to='inventory/images')  
    
    def __str__(self):
        return self.name