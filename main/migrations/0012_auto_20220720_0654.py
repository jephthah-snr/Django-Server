# Generated by Django 3.1.7 on 2022-07-20 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20220720_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eb5',
            name='amount',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='eb5',
            name='percentage',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
