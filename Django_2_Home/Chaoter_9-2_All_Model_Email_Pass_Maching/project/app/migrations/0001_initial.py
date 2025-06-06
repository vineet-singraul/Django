# Generated by Django 5.2 on 2025-04-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_phone', models.IntegerField()),
                ('stu_dob', models.DateField()),
                ('stu_password', models.CharField(max_length=50)),
                ('stu_cpassword', models.CharField(max_length=50)),
                ('stu_gender', models.CharField(max_length=60)),
                ('stu_subscribe', models.CharField(max_length=60)),
                ('stu_detail', models.CharField(max_length=60)),
                ('stu_image', models.ImageField(upload_to='image')),
                ('stu_resume', models.FileField(upload_to='image')),
            ],
        ),
    ]
