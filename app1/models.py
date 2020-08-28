from django.db import models
class Product(models.Model):
    idno=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Price=models.IntegerField()
    Quantity=models.IntegerField()
    Picture=models.ImageField(upload_to='myproducts/')
    file=models.FileField(default=False,upload_to='myfiles/')

# Create your models here.
