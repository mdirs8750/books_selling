# Generated by Django 3.2.9 on 2022-02-02 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apbook', '0005_alter_uploadimg_pimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimg',
            old_name='product',
            new_name='productname',
        ),
    ]
