# Generated by Django 3.2 on 2021-05-29 18:42

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_game_price'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='game',
            name='price_gt_0',
        ),
        migrations.AddConstraint(
            model_name='game',
            constraint=models.CheckConstraint(check=models.Q(price__gte=Decimal('0')), name='price_gte_0'),
        ),
    ]
