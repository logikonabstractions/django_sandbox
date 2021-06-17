from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    is_atest = models.BooleanField(default=True)

# Create your models here.
class Foo(models.Model):
    my_attr = models.CharField(max_length=50)

class Bar(models.Model):
    fk = models.ForeignKey(Foo, on_delete=models.CASCADE)
    secondary_attr = models.IntegerField(default=42)

class Ent(models.Model):
    ent_1 = models.CharField(max_length=40)
    ent_2 = models.CharField(max_length=40)
    ent_3 = models.CharField(max_length=40)

class Det(models.Model):
    fk_ent = models.ForeignKey(to=Ent, on_delete=models.CASCADE, related_name="dets")
    det_1 = models.IntegerField()
    det_2 = models.IntegerField()
    det_3 = models.IntegerField()
