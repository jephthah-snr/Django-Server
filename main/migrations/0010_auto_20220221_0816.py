# Generated by Django 3.2.7 on 2022-02-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_transaction_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='amount',
            new_name='amount_btc',
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount_num',
            field=models.IntegerField(default=12345678, max_length=20),
            preserve_default=False,
        ),
    ]
