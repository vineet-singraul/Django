# Generated by Django 5.2 on 2025-04-24 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contect', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emplyee',
            fields=[
                ('baseinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.baseinfo')),
                ('department', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
            ],
            bases=('app.baseinfo',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('baseinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.baseinfo')),
                ('branch', models.CharField(max_length=40)),
                ('fees', models.IntegerField()),
            ],
            bases=('app.baseinfo',),
        ),
    ]
