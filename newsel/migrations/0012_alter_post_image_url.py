# Generated by Django 3.2.23 on 2024-02-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsel', '0011_alter_post_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='لینک تصویر'),
        ),
    ]
