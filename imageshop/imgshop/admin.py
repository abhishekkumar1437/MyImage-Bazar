from django.contrib import admin
from .models import Category,image
# Register your models here.
from .views import *

admin.site.register(Category)
admin.site.register(image)
