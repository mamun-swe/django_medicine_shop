# Generated by Django 3.0.7 on 2020-06-24 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0003_auto_20200624_0344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='status',
            new_name='order_status',
        ),
    ]
