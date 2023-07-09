from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from trading.models import Trading
import time
from trading.models import UserProfile,CoinPurchase,Transaction
from decimal import Decimal
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#import lstm as ls  # Assuming `model` is the name of the saved LSTM model in lstm.py
from tensorflow.python.keras.models import load_model
from django.db.models import Max











def evaluate_model(y_true, y_pred):
    # Calculate Mean Squared Error (MSE)
    mse = mean_squared_error(y_true, y_pred)

    # Calculate Root Mean Squared Error (RMSE)
    rmse = np.sqrt(mse)

    # Calculate R-squared (R²)
    r2 = r2_score(y_true, y_pred)

    # Print the evaluation metrics
    print("Mean Squared Error (MSE):", mse)
    print("Root Mean Squared Error (RMSE):", rmse)
    print("R-squared (R²):", r2)








@login_required(login_url='login')
def platform_coin(request):
    response_data = {}
    coin_name = "BTC"
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If the user profile doesn't exist, create a new one
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        # Get the amount of coins from the form
        coins_to_buy = request.POST.get('coin')
        coin=request.POST.get('inr')
        print(coins_to_buy)
        

        balance = user_profile.balance 
        print("balance =====",balance)
         # Access the actual value of the balance attribute
        
        coins=Decimal(coin)

        if coins <= balance:
            # Update the coins count
            user_profile.balance = user_profile.balance - coins
            
            coins_to_buy_decimal = Decimal(coins_to_buy)
            user_profile.coins += coins_to_buy_decimal
            user_profile.save()

            coin_purchase = CoinPurchase(user=request.user, coin_name=coin_name, quantity=coins_to_buy)
            coin_purchase.save()

            print(user_profile.coins)
            response_data['coins'] = str(user_profile.coins)  # Convert Decimal to string for JSON response
        else:
        # Clear the input value when the page is reloaded
            messages.warning(request, 'Wallet balance is low.')
         


    return render(request, 'platform.html', {'messages': messages.get_messages(request)})



def add_cash(request):
    
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If the user profile doesn't exist, create a new one
        user_profile = UserProfile(user=request.user)
        user_profile.save()
    if request.method == 'POST':
        # Get the amount of coins from the form
        cash = request.POST.get('cash')
        print(cash)

        if cash:
            
            user_profile.balance += Decimal(cash)
            user_profile.save()

    return render(request, 'platform.html')



def logout_view(request):
    logout(request)
    return redirect('login')



def transaction_table_view(request):
    data = CoinPurchase.objects.all()
    data = data.values('coin_name', 'quantity', 'purchase_date')
    serialized_data = list(data)
    return JsonResponse(serialized_data, safe=False)

def dataset_view(request):
    dat = Trading.objects.all()
    data = dat.values('Date','Open', 'Close','Marketcap','Volume')
    serialized_data = list(data)
    return JsonResponse(serialized_data, safe=False)

          

def get_Dynamiccoin(request):

    user_profile =UserProfile.objects.get(user=request.user)  # Assuming a related_name of 'userprofile' in the UserProfile model
    coins = user_profile.coins
    balance = user_profile.balance
    try:
     latest_date = Trading.objects.aggregate(latest_date=Max("Date"))["latest_date"]
     latest_close = Trading.objects.filter(Date=latest_date).values_list("Close", flat=True).first()

     #dynamic_value = latest_close


     data = {'Close': latest_close}
     # render(request, 'coins.html', {'coins': coins})
     print(coins)
     return JsonResponse({'dynamic_value': coins,'data':data,'balance':balance})
            
    except Trading.DoesNotExist:
        return JsonResponse({'error': 'No data found'}, status=404)
    


    



def price(request):
    try:
        # Retrieve the last updated row from the database
        #last_updated_data = Trading.objects.first()
        latest_date = Trading.objects.aggregate(latest_date=Max("Date"))["latest_date"]
        latest_close = Trading.objects.filter(Date=latest_date).values_list("Close", flat=True).first()

        dynamic_value = latest_close

         # return JsonResponse({'dynamic_value': dynamic_value})

        #close_value=last_updated_data.Close if last_updated_data else None

        # Get the value from the 'close' column
       # close_value = last_updated_data.Close

        # Prepare the data to be sent as a JSON response
        response_data = {
            'Close': dynamic_value,
        }

        return JsonResponse(response_data)
    except Trading.DoesNotExist:
        return JsonResponse({'error': 'No data found'}, status=404)

def data_endpoint(request):
    # Retrieve the updated data from the database


    datas = Trading.objects.all()[:600]

    # Fetching only the 'open' and 'close' columns
    data = datas.values('Date','Open','High','Low', 'Close')

    #data = Trading.objects.all().values('Open', 'Close')  # Replace 'date' and 'close_price' with the actual field names in your model
    
    

    # Convert the data to a dictionary or list to be serialized as JSON
    serialized_data = list(data)  # Use list() to convert the queryset to a list of dictionaries
    

   
    # Return the serialized data as JSON response
    
    return JsonResponse(serialized_data,safe=False)

@login_required(login_url='login')
def home (request):
    return render(request,'index.html')

def get_dynamic_value(request):

    
    latest_date = Trading.objects.aggregate(latest_date=Max("Date"))["latest_date"]
    latest_close = Trading.objects.filter(Date=latest_date).values_list("Close", flat=True).first()

    dynamic_value = latest_close

    return JsonResponse({'dynamic_value': dynamic_value})

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass')
        print(uname,email,pass1)

        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')

    return render(request,'signup.html')


def Login(request):
   
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password is incorrect')
    
    return render(request,'login.html')
   
@login_required(login_url='login')
def platform(request):
    return render(request,'platform.html')


def usern(request):
    username=request.user.username
    return JsonResponse(username,safe=False)