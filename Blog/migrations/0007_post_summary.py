# Generated by Django 3.2.2 on 2021-05-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_post_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
