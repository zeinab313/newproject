# Generated by Django 3.2.23 on 2024-02-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsel', '0018_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='trash',
            field=models.BooleanField(default=False, null=True, verbose_name='زباله دان'),
        ),
    ]
