# Generated by Django 4.2.8 on 2024-01-02 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipoFutbol',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('equipo', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'db_table': 'equipos_de_futbol',
            },
        ),
    ]
