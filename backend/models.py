from django.db import models

# Create your models here.
class Category(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        db_table='category'

class Brand(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)
    image_path=models.ImageField(upload_to='brand',null=True,blank=True,default="no_image_available.png")

    def __str__(self):
        return self.name
    class Meta:
        db_table='brand'