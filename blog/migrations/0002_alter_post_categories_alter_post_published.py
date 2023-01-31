# Generated by Django 4.1.5 on 2023-01-15 04:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_posts', to='blog.category', verbose_name='Categorías'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 15, 4, 52, 38, 817617, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicación'),
        ),
    ]