# Generated by Django 3.2.23 on 2024-02-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsel', '0021_auto_20240217_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='h1',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='تگ h1'),
        ),
    ]
