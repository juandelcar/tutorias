# Generated by Django 5.0.2 on 2024-06-04 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_remove_question_question_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer1',
            field=models.CharField(max_length=200, verbose_name='Respuesta A'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer2',
            field=models.CharField(max_length=200, verbose_name='Respuesta B'),
        ),
    ]
