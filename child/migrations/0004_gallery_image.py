# Generated by Django 3.2.18 on 2023-03-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0003_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery'),
        ),
    ]