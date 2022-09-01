# Generated by Django 3.2.15 on 2022-09-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_add_job_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='situation',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='Pending', max_length=50, null=True),
        ),
    ]
