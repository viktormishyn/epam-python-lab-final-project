# Generated by Django 3.2 on 2021-05-20 14:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210520_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
