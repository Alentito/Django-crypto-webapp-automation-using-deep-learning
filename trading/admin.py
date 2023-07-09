from django.contrib import admin
from trading.models import Trading
from trading.models import UserProfile,CoinPurchase,Transaction



class TradingAdmin(admin.ModelAdmin):
    list_display=('id','Date','Open','Close','Marketcap','Volume')



admin.site.register(Trading,TradingAdmin)
# Register your models here.




class UserProfileAdmin(admin.ModelAdmin):
    list_display=('id','user','coins','balance')

admin.site.register(UserProfile,UserProfileAdmin)


class CoinPurchaseAdmin(admin.ModelAdmin):
    list_display=('id','user','coin_name','quantity','purchase_date')

admin.site.register(CoinPurchase,CoinPurchaseAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display=('user_profile','trade_type','cryptocurrency','quantity','price','volatility','drawdown','risk_reward_ratio','created_at')

admin.site.register(Transaction,TransactionAdmin)