# Generated by Django 2.0.2 on 2019-01-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acordemos', '0008_auto_20190112_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votacion',
            name='voto',
            field=models.IntegerField(choices=[(1, 'Aprueba'), (-1, 'No Aprueba'), (0, 'Abstiene')], default=1),
        ),
    ]
