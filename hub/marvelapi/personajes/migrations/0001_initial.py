# Generated by Django 3.1.2 on 2020-10-21 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128, null=True)),
                ('nombre_real', models.CharField(max_length=128)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
