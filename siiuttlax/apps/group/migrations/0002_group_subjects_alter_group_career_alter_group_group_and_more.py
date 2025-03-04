# Generated by Django 5.0.6 on 2024-06-11 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
        ('career', '0004_alter_subject_options'),
        ('group', '0001_initial'),
        ('period', '0002_alter_period_options_alter_semester_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='career.subject', verbose_name='Materias'),
        ),
        migrations.AlterField(
            model_name='group',
            name='career',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'), ('G', 'G'), ('H', 'H')], default='A', max_length=1, verbose_name='Grupo'),
        ),
        migrations.AlterField(
            model_name='group',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.period', verbose_name='Periodo'),
        ),
        migrations.AlterField(
            model_name='group',
            name='semester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='period.semester', verbose_name='Cuatrimestre'),
        ),
        migrations.AlterField(
            model_name='group',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.professor', verbose_name='Tutor'),
        ),
    ]
