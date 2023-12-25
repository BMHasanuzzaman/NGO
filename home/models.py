from django.db import models


# Create your models here.
class Image(models.Model):

    image=models.ImageField(upload_to="img/%y")

    class Meta:
        ordering=('-id',)





class Hurricane(models.Model):
    image=models.ImageField(upload_to="img/%y")
    date=models.DateTimeField()
    user_name=models.CharField(max_length=10)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)

    class Meta:
        ordering=('-id',)

    def __str__(self):
         return self.user_name


class Causers(models.Model):
    image = models.ImageField(upload_to="img/%y")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    donation = models.CharField(max_length=30)
    count = models.CharField(max_length=30)

    class Meta:
        ordering=('-id',)
    def __str__(self):
         return self.title

class contactInfo(models.Model):
        name=models.CharField(max_length=25)
        email=models.CharField(max_length=40)
        subject=models.CharField(max_length=15)
        message=models.CharField(max_length=200)


class Donation(models.Model):
    donor_name = models.CharField(max_length=255)
    email = models.EmailField()
    number= models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Number(models.Model):
   amount = models.CharField(max_length=20)

