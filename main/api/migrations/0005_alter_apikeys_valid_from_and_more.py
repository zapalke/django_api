# Generated by Django 5.0.7 on 2024-08-03 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_apikeys_valid_from_alter_requestlog_api_key_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apikeys",
            name="valid_from",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 8, 3, 9, 16, 46, 890268, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="requestlog",
            name="request_time",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 8, 3, 9, 16, 46, 891245, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
