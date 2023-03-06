# Generated by Django 3.2.18 on 2023-03-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='childinfo',
            name='currentcity',
            field=models.CharField(choices=[('Delhi', 'DELHI'), ('Mumbai', 'MUMBAI'), ('Ahmedabad', 'Ahmedabad'), ('Kolkata', 'KOLKATA')], default='Not known', max_length=10),
        ),
    ]
