# Generated by Django 5.0.6 on 2024-05-28 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_patient_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="password",
            field=models.CharField(default="fdfd", max_length=100),
            preserve_default=False,
        ),
    ]
