# Generated by Django 3.2.23 on 2024-02-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsel', '0019_alter_post_trash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='confirm_to_post',
            field=models.BooleanField(default=False, null=True, verbose_name='پست تایید شده؟'),
        ),
    ]
