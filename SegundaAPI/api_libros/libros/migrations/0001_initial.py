# Generated by Django 3.1.2 on 2020-10-28 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=1000)),
                ('genero', models.CharField(default='', max_length=200)),
                ('autor', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
