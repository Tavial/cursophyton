# Generated by Django 3.0.6 on 2020-05-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0003_auto_20200508_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('clave', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
            ],
        ),
    ]
