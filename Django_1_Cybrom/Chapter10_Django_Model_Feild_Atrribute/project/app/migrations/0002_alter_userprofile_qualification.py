# Generated by Django 5.2 on 2025-04-23 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Qualification',
            field=models.CharField(choices=[('B-Tech', 'B-Tech'), ('M-Tech', 'M-Tech')], db_index=True, max_length=100, null=True, verbose_name='Quali'),
        ),
    ]
