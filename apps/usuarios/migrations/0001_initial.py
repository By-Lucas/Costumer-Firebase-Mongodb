# Generated by Django 4.0.1 on 2022-03-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome_user', models.CharField(max_length=20)),
                ('sobrenome_user', models.CharField(max_length=70)),
            ],
        ),
    ]
