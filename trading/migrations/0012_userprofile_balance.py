# Generated by Django 4.2.1 on 2023-06-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0011_delete_coin'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=20),
        ),
    ]
