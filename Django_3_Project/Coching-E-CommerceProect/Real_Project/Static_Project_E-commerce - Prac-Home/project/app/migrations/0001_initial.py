# Generated by Django 5.2 on 2025-04-27 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=60)),
                ('cus_email', models.EmailField(max_length=254, unique=True)),
                ('cus_password', models.CharField(max_length=50)),
                ('cus_cpassword', models.CharField(max_length=50)),
                ('cus_image', models.ImageField(upload_to='image')),
                ('cus_phone', models.IntegerField()),
                ('cus_location', models.CharField(max_length=50)),
            ],
        ),
    ]
