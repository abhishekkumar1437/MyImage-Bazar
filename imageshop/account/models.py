from django.db import models
from django.contrib.auth.models import User
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields import CharField

# Create your models here.
class signup_user(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    password=models.TextField()
    cpassword=models.TextField()

class Meta:
        model = User
        fields = ('email', 'name', 'password', 'cpassword', )