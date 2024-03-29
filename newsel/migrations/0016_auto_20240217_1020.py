# Generated by Django 3.2.23 on 2024-02-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsel', '0015_alter_post_folder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=250, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publisher',
            field=models.CharField(max_length=250, verbose_name='ناشر'),
        ),
        migrations.AlterField(
            model_name='post',
            name='source_website',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='منبع خبر'),
        ),
        migrations.AlterField(
            model_name='post',
            name='supervisor_to_confirm',
            field=models.CharField(max_length=250, null=True, verbose_name='سرپرست تایید کننده پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='post',
            name='type_of_news',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='نوع خبر'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='لینک'),
        ),
    ]
