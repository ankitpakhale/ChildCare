# Generated by Django 3.2.18 on 2023-03-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0006_delete_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='isPaid',
            field=models.BooleanField(default=False),
        ),
    ]