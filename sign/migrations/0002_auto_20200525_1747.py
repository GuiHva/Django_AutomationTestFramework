# Generated by Django 3.0.6 on 2020-05-25 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sign.Event'),
        ),
    ]
