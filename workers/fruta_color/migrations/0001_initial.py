# Generated by Django 4.2.8 on 2024-01-01 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrutaColor',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('fruta', models.CharField(blank=True, default='', max_length=100)),
                ('color', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'db_table': 'Fruta y Color',
            },
        ),
    ]
