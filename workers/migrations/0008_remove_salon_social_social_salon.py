# Generated by Django 4.0.4 on 2022-06-02 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0007_remove_salon_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salon',
            name='social',
        ),
        migrations.AddField(
            model_name='social',
            name='salon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='salons.salon', verbose_name='Салон'),
            preserve_default=False,
        ),
    ]
