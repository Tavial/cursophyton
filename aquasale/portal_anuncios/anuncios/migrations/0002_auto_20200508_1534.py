# Generated by Django 3.0.6 on 2020-05-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='id_categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='anuncio',
            old_name='id_tipo',
            new_name='tipo',
        ),
        migrations.AddField(
            model_name='anuncio',
            name='fecha',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anuncio',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotografias'),
        ),
    ]
