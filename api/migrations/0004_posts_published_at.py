# Generated by Django 4.0.4 on 2022-05-25 04:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_posts_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
