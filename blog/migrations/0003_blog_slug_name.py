# Generated by Django 2.2.5 on 2019-09-29 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]