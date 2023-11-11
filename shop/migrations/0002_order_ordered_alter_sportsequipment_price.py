# Generated by Django 4.2.7 on 2023-11-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sportsequipment',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]