# Generated by Django 3.0.6 on 2020-05-25 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_auto_20200525_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign.Event'),
        ),
    ]
