# Generated by Django 3.2.2 on 2021-05-14 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscriber_model',
            new_name='Subscribers',
        ),
        migrations.AlterModelTable(
            name='subscribers',
            table='Blog_subscribers',
        ),
    ]
