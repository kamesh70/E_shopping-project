from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
STATE_CHOICES=(
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES=(
        ('M','Mobile'),
        ('L','Laptop'),
        ('TW','Top Wear'),
        ('BW','Bottom Ware'),
    )

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description= models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price    

STATUS_CHOICES=(
    ('Accepted','Accepted'),
     ('Packed','Packed'),
      ('On the way','On the way'),
       ('Delivered','Delivered'),
)
    

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    quantity=models.PositiveIntegerField(default=1)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    
    ordered_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default="Accepted")

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price    

    
