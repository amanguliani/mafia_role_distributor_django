# Generated by Django 3.0.6 on 2020-05-11 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=30)),
                ('game_name', models.CharField(max_length=30)),
                ('role_assigned', models.CharField(max_length=30)),
            ],
        ),
    ]