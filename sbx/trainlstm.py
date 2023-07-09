from lstm import train_lstm_model
import pandas as pd

# Load the data
data = pd.read_csv('static/csv/coin_Bitcoin.csv')

# Train the LSTM model and save it
model = train_lstm_model(data)
model.save('C:/Users/imale/Documents/Projects/sbx/sbx/model.h5')
