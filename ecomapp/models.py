from django.db import models
from django.contrib.auth.models import User # TODO: Using username is the default password  

class Product(models.Model):
    """Customer can create product"""
    PRODUCT_CATEGORY = (('1', 'Electronics'), 
                        ('2', 'Fashion'), 
                        ('3', 'Home Appliances'), 
                        )
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=2, choices=PRODUCT_CATEGORY, default='1'
                                ) # TODO: This field should be replaced with relation table in future
    image = models.ImageField(upload_to='images/product/') # TODO: Image format and size should be added to the actual context
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"product: {self.name} | id: {self.id} | price: {self.price} | category: {self.category}"

