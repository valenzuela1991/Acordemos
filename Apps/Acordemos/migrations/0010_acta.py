# Generated by Django 2.0.2 on 2019-01-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acordemos', '0009_auto_20190112_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('media', models.FileField(upload_to='')),
                ('descripcion', models.TextField()),
                ('FK_Acuerdo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Acordemos.Acuerdo')),
            ],
        ),
    ]
