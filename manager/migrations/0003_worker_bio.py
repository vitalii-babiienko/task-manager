# Generated by Django 4.2.3 on 2023-07-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0002_alter_worker_position"),
    ]

    operations = [
        migrations.AddField(
            model_name="worker",
            name="bio",
            field=models.TextField(default="Here you can add some bio about you ;)"),
        ),
    ]