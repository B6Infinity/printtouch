# Generated by Django 4.1 on 2023-07-13 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0003_remove_flow_pd_amt_remove_flow_pd_upcoming_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pd_amt',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
