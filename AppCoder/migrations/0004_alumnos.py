# Generated by Django 5.0.3 on 2024-03-31 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_profesores_alter_curso_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('camada', models.IntegerField()),
            ],
            options={
                'db_table': 'AppCoder_alumnos',
            },
        ),
    ]