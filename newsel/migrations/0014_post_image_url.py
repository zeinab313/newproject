# Generated by Django 3.2.23 on 2024-02-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsel', '0013_remove_post_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='لینک تصویر'),
        ),
    ]