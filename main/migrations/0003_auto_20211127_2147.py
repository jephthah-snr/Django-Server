# Generated by Django 3.2.7 on 2021-11-27 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211116_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('data', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='accountbalance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bitcoinbalance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bouncerate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='percentageincrease',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]