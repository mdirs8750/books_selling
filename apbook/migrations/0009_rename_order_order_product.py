# Generated by Django 3.2.9 on 2022-02-15 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apbook', '0008_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='product',
        ),
    ]
