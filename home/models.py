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