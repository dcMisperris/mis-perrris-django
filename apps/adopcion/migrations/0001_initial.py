# Generated by Django 2.1.3 on 2018-11-08 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotografia', models.ImageField(upload_to='static/img/')),
                ('nombre', models.CharField(max_length=30)),
                ('raza_predominante', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('Rescatado', 'Rescatado'), ('Disponible', 'Disponible'), ('Adoptado', 'Adoptado')], default='Rescatado', max_length=15)),
            ],
        ),
    ]
