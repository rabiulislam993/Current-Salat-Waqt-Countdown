# Generated by Django 2.0.6 on 2018-06-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countdown', '0002_auto_20180616_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthwisewaqtstring',
            name='month',
            field=models.CharField(help_text='month number from 1 to 12', max_length=2),
        ),
        migrations.AlterField(
            model_name='waqt',
            name='asr',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='waqt',
            name='day',
            field=models.CharField(blank=True, help_text='unix format for day (%d)', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='waqt',
            name='fazr',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='waqt',
            name='isha',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='waqt',
            name='juhr',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='waqt',
            name='magrib',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='waqt',
            name='month',
            field=models.CharField(blank=True, help_text='unix format for month (%m)', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='waqt',
            name='sunrise',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
