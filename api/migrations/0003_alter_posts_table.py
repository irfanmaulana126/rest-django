# Generated by Django 4.0.4 on 2022-05-25 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_posts_created_at_posts_updated_at'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='posts',
            table='posts',
        ),
    ]
