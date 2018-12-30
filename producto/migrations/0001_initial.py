# Generated by Django 2.1.4 on 2018-12-30 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=1, max_digits=6)),
                ('imagen', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
