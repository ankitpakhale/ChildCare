# Generated by Django 3.1.5 on 2023-03-02 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('state', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=30)),
                ('Address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='cci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('currentcity', models.CharField(max_length=50)),
                ('no_of_children', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='childinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('currentcity', models.CharField(choices=[('Delhi', 'DELHI'), ('Mumbai', 'MUMBAI'), ('Gujarat', 'GUJARAT'), ('Kolkata', 'KOLKATA')], default='Not known', max_length=10)),
                ('aadhar', models.BooleanField(default=False)),
                ('dob', models.DateField(max_length=8)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='childs')),
                ('guardian', models.CharField(max_length=50)),
                ('cci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_of_children', to='child.cci')),
            ],
        ),
        migrations.CreateModel(
            name='donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('Gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], default=None, max_length=10)),
                ('Address', models.CharField(max_length=500)),
                ('Occupation', models.CharField(max_length=50)),
                ('Emailid', models.CharField(max_length=50)),
                ('Bank_account_no', models.CharField(max_length=25)),
                ('IFSC_code', models.CharField(max_length=20)),
                ('Aadharcardno', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='lostchild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cityfound', models.CharField(max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='lostchild')),
                ('Detail', models.CharField(max_length=100000)),
                ('guardian', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='typecci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('userid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('Gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], default=None, max_length=10)),
                ('Martialstatus', models.CharField(choices=[('Married', 'MARRIED'), ('unmarried', 'UNMARRIED'), ('divorced', 'DIVORCED')], default='unmarried', max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('Job_description', models.CharField(max_length=5000)),
                ('adoptionreason', models.CharField(max_length=5000)),
                ('aadhar', models.BooleanField(default=False)),
                ('childwanted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childwanted', to='child.childinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='child.post')),
            ],
        ),
        migrations.AddField(
            model_name='cci',
            name='typ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_of_cci', to='child.typecci'),
        ),
    ]