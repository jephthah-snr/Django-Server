from django.db import models
from django.utils import timezone

class AccountBalance(models.Model):
    balance = models.CharField(max_length=200)

    def __str__(self):
        return "Account balance"


class BitcoinBalance(models.Model):
    balance = models.DecimalField(decimal_places=12, max_digits=13)

    def __str__(self):
        return "Bitcoin balance"


class BounceRate(models.Model):
    balance = models.IntegerField(default=2400)

    def __str__(self):
        return "Bounce rate"

class PercentageIncrease(models.Model):
    balance = models.IntegerField(default=5)

    def __str__(self):
        return "Percentage increase"

class Activity(models.Model):
    name = models.CharField(max_length=80)
    operation = models.CharField(max_length=80)
    date = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Notification(models.Model):
    title = models.CharField(max_length=80)
    data = models.CharField(max_length=80)
    date = models.CharField(max_length=30)


    def __str__(self):
        return "notifications"


class BtcSales(models.Model):
    sell = models.DecimalField(decimal_places=12, max_digits=13)
    buys = models.DecimalField(decimal_places=12, max_digits=13)
    def __str__(self):
        return self.buys


class Transaction(models.Model):
    amount_btc = models.DecimalField(decimal_places=12, max_digits=13)
    amount_num = models.IntegerField(max_length=20)
    wallet_id = models.CharField(default="15f5s8s47bhj61r8w4e77e5e56", max_length=80)
    date = models.CharField(max_length=30)

    def __str__(self):
        return self.wallet_id


class eb5(models.Model):
    amount = models.CharField(max_length=8)
    percentage = models.DecimalField(decimal_places=1, max_digits=4)

    def __str__(self):
        amt = str(self.amount)
        return amt