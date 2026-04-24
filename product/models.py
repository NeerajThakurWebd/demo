from django.db import models
from tinymce.models import HTMLField

class Product(models.Model):
    product_image = models.ImageField(upload_to='products/')
    product_name=models.CharField(max_length=50)
    product_des=HTMLField()
    product_prize=models.CharField(max_length=50)

# Create your models here.


