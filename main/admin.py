from django.contrib import admin
from . models import AccountBalance, BitcoinBalance, BounceRate, BtcSales, PercentageIncrease, Activity, Notification, Transaction,BtcSales, Transaction, eb5

# Register your models here.
admin.site.register(AccountBalance)

admin.site.register(BitcoinBalance)

admin.site.register(BounceRate)

admin.site.register(PercentageIncrease)

admin.site.register(Activity)

admin.site.register(Notification)

admin.site.register(BtcSales)

admin.site.register(Transaction)

admin.site.register(eb5)



