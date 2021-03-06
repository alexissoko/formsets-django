# Generated by Django 3.0.6 on 2020-05-20 03:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('gender', models.CharField(choices=[('0', 'Varon'), ('1', 'Mujer'), ('2', 'Otro')], max_length=1, verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumno.Alumno')),
            ],
            options={
                'verbose_name': 'Asistencia',
                'verbose_name_plural': 'Asistencias',
            },
        ),
    ]
