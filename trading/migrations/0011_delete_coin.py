# Generated by Django 4.2.1 on 2023-06-25 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0010_alter_coinpurchase_id_alter_coinpurchase_quantity_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coin',
        ),
    ]
