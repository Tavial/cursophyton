# Generated by Django 3.1.2 on 2020-10-28 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='tapa_dura',
            field=models.BooleanField(default=False),
        ),
    ]
