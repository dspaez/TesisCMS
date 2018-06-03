# Generated by Django 2.0.5 on 2018-05-27 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonumentosQuito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.CharField(max_length=200)),
                ('nombre_monumento', models.CharField(max_length=200)),
                ('descripcion_monumento', models.TextField(max_length=2000)),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('imagen_antigua', models.ImageField(upload_to='imagenes/')),
            ],
        ),
    ]