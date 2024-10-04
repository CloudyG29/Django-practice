from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    description=models.TextField(max_length=10000)
    image=models.ImageField(upload_to='product_images/',blank=True, null=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    product=models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return f"stock for {self.product.name}: {self.quantity} units"


class Order(models.Model):
    date=models.DateTimeField()
    total_amount=models.DecimalField(max_digits=10, decimal_places=2)  
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

