# Generated by Django 2.1.4 on 2018-12-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0007_auto_20181205_0234'),
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
