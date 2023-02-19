from io import BytesIO
from PIL import Image
from django.core.files import FIle

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta : 
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    
class Product(models.Model):
    # the schema models is if the category deleted the product also deleted, it's the meaning on on delete cascade
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    

