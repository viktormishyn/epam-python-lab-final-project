# Generated by Django 3.2 on 2021-05-14 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='about',
        ),
    ]