from django.db import models


class Review(models.Model):
    description = models.TextField()
    

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    reviews = models.ForeignKey(Review,null=True,blank=True)

    def __str__(self):
        return self.name