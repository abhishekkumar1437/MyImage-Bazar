# Generated by Django 3.2.8 on 2021-10-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgshop', '0003_remove_image_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('img_id', models.IntegerField(null=True)),
                ('like', models.IntegerField(null=True)),
            ],
        ),
    ]
