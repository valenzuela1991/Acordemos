# Generated by Django 2.0.2 on 2019-01-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acordemos', '0005_auto_20190112_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votacion',
            name='voto',
            field=models.CharField(choices=[(1, 'Aprueba'), (-1, 'No Aprueba'), (0, 'Abstiene')], default=1, max_length=10),
        ),
    ]
