# Generated by Django 3.1.2 on 2020-10-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_libro_tapa_dura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido')),
            ],
        ),
    ]
