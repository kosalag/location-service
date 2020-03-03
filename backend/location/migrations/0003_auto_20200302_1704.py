# Generated by Django 3.0.3 on 2020-03-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_policedivisions_policestations_provincialministries_provincialministrydemartments'),
    ]

    operations = [
        migrations.AddField(
            model_name='commissions',
            name='code',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departments',
            name='code',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ministries',
            name='code',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
