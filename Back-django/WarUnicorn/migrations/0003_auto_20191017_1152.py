# Generated by Django 2.2.6 on 2019-10-17 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("WarUnicorn", "0002_auto_20191017_1022")]

    operations = [
        migrations.RemoveField(model_name="unicorn", name="language"),
        migrations.RemoveField(model_name="unicorn", name="style"),
    ]
