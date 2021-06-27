from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.
STATE_CHOICE=(
  ('West Bengal','West Bengal'),
  ('West Bengal2','West Bengal2'),
  ('West Bengal3','West Bengal3'),
  ('West Bengal4','West Bengal4'),

)

# customer
class Customer(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  name=models.CharField(max_length=200)
  locality=models.CharField(max_length=200)
  city=models.CharField(max_length=50)
  zipcode=models.IntegerField()
  state=models.CharField(choices=STATE_CHOICE,max_length=50)
  def __str__(self):
      return str(self.id)
  

# product
CATAGORY=(
  ('M','Mobile'),
  ('L','Laptop'),
  ('TW','Top Ware'),
  ('BW','Bottom Ware')
)

class Product(models.Model):
  title=models.CharField(max_length=100)
  seeling_price=models.FloatField()
  discount_price=models.FloatField()
  brand=models.CharField(max_length=100)
  description=models.TextField()
  catagory=models.CharField(choices=CATAGORY,max_length=2)
  product_image=models.ImageField( upload_to='productimg')
  def __str__(self):
      return str(self.id)

   
class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  quantity=models.PositiveIntegerField(default=1)
  def __str__(self):
      return str(self.id)
  
  @property
  def price(self):
    return int(self.quantity*self.product.discount_price  )     
  

# order placed
STATUS_CHOICE=(
  ('Accepted','Accepted'),
  ('Packed','Packed'),
  ('On The Way','On The Way'),
  ('Delivered','Delivered'),
  ('Cancel','Cancel'),
)
class OrerPlaced(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  quantity=models.PositiveIntegerField(default=1)
  order_date=models.DateField(auto_now_add=True)
  price=models.PositiveIntegerField(default=1)
  status=models.CharField(max_length=50,choices=STATUS_CHOICE,default='pendeng')

