# Generated by Django 3.2.8 on 2021-10-23 23:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imgshop', '0007_auto_20211023_2253'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Image_Likes',
        ),
    ]
