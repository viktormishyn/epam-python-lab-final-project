# Generated by Django 3.2 on 2021-05-11 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.genre', to_field='name'),
        ),
    ]
