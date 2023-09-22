from django.db import models

# Create your models here.
class Sneaker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=200)
    price = models.IntegerField('Price')
    link = models.CharField('Link' , max_length=200)

    def __str__(self):
        return f"id: {self.id}| Nom :{self.name}|Prix :{self.price} " 