# Generated by Django 4.2.9 on 2024-02-08 11:20

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='pet_photos/', validators=[petstagram.photos.validators.validate_photo_size_less_than_5mb]),
        ),
    ]
