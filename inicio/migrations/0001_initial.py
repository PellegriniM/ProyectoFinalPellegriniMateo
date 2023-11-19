# Generated by Django 4.2.6 on 2023-11-19 02:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=30)),
                ('asunto', models.CharField(max_length=30)),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('fecha_creacion', models.DateField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]
