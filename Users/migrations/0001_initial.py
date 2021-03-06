# Generated by Django 3.2.2 on 2021-05-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber_model',
            fields=[
                ('Sys_Id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=150, unique=True)),
                ('status', models.CharField(blank=True, max_length=64)),
                ('created_date', models.DateTimeField(blank=True)),
                ('updated_date', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'Users_subscribe',
            },
        ),
    ]
