# Generated by Django 5.1.1 on 2024-09-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('designer', 'designer'), ('user', 'user')], default='user', max_length=100),
        ),
    ]
