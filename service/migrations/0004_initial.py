# Generated by Django 4.0.4 on 2022-06-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0003_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название услуги')),
                ('duration', models.CharField(max_length=256, verbose_name='Продолжительность')),
            ],
        ),
    ]
