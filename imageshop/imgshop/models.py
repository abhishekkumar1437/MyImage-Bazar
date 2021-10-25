from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.title

class image(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField()
    cate=models.ForeignKey(Category,on_delete=models.CASCADE)
    like=models.IntegerField(null=True)


    def __str__(self):
        return self.title

class Image_Likes(models.Model):
    likes = models.ManyToManyField(User, related_name='image_like')

    def number_of_likes(self):
        return self.likes.count()