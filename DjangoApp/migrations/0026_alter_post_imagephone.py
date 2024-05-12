# Generated by Django 5.0.3 on 2024-05-13 01:53

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0025_alter_post_imagephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagePhone',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=70, scale=None, size=[300, 200], upload_to='phone'),
        ),
    ]
