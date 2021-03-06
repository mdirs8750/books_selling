# Generated by Django 3.2.9 on 2022-02-03 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apbook', '0006_rename_product_uploadimg_productname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='upload/productimg')),
                ('price', models.IntegerField(default=100)),
                ('Description', models.CharField(default=100, max_length=255)),
                ('Category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apbook.category')),
            ],
        ),
        migrations.DeleteModel(
            name='uploadimg',
        ),
    ]
