# Generated by Django 2.1.3 on 2018-11-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0005_auto_20181126_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='mail',
            field=models.EmailField(default='mail@mail.cl', max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(default='Name-def', max_length=30),
        ),
        migrations.AlterField(
            model_name='persona',
            name='passwd',
            field=models.CharField(default='1234', max_length=40),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.CharField(default='1111-1', max_length=9),
        ),
    ]