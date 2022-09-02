# Generated by Django 3.2.15 on 2022-09-02 18:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_add_file_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='age',
        ),
        migrations.AddField(
            model_name='candidate',
            name='birth',
            field=models.DateField(default=datetime.datetime(2022, 9, 2, 18, 23, 28, 568996, tzinfo=utc), verbose_name='Birthday'),
            preserve_default=False,
        ),
    ]
