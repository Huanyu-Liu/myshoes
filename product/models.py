from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Username(User):
    # def create_user(self,username,password):
    #     self.username = username
    #     self.password = password

    class Meta:
        proxy = True
    # username = models.EmailField()
    # password = models.CharField(max_length=20)

class Product(models.Model):
    gender = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    img = models.FileField(upload_to='product/')

class Cart(models.Model):
    count = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    user = models.ForeignKey(Username)
    product = models.ForeignKey(Product)
    size = models.IntegerField(default=40)

