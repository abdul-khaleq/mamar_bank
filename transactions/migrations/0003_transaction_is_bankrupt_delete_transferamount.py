# Generated by Django 4.2.7 on 2024-01-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transferamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_bankrupt',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='TransferAmount',
        ),
    ]
