from django.contrib.auth.models import User
from django.db import models



# Create your models here.

class Trading(models.Model):
     id = models.AutoField(primary_key=True)
     Date = models.DateField()
     High=models.FloatField()
     Low=models.FloatField()
     Open = models.FloatField()
     Close = models.FloatField()
     Volume = models.FloatField()
     Marketcap = models.FloatField()
     

     def __str__(self):
        return f'{self.Date} - Open: {self.High}, Open: {self.Low}, Open: {self.Open}, Close: {self.Close}, Volume: {self.Volume}, Market Cap: {self.Marketcap} '




class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.DecimalField(default=0, max_digits=20, decimal_places=10)
    balance= models.DecimalField(default=0, max_digits=20, decimal_places=10)





class CoinPurchase(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin_name = models.CharField(max_length=50)
    quantity = models.DecimalField(default=0, max_digits=20, decimal_places=10)
    purchase_date = models.DateTimeField(auto_now_add=True)



class Transaction(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    trade_type = models.CharField(max_length=10)
    cryptocurrency = models.CharField(max_length=10)
    quantity = models.FloatField()
    price = models.FloatField()
    volatility = models.FloatField(null=True)
    drawdown = models.FloatField(null=True)
    risk_reward_ratio = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)