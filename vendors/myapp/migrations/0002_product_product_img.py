# Generated by Django 5.0.7 on 2024-07-20 09:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=None),
            preserve_default=False,
        ),
    ]
