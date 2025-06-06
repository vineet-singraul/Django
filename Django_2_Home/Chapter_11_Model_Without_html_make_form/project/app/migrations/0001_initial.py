# Generated by Django 5.2 on 2025-04-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, help_text='Enter a unique username', max_length=50, null=True, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('bio', models.CharField(blank=True, db_index=True, help_text='Write a short bio about yourself', max_length=50, null=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('Qualification', models.CharField(choices=[('1', 'B-tech'), ('2', 'M-tech'), ('3', 'P-hd'), ('4', 'Diploma')], db_index=True, max_length=100, null=True, verbose_name='Quali')),
            ],
        ),
    ]
