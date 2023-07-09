import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split

# Load CSV data into a Pandas dataframe
data = pd.read_csv('static/csv/coin_Bitcoin.csv')

# Step 1: Preprocessing the Data
# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Normalize numerical columns
scaler = MinMaxScaler()
columns_to_normalize = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']
data[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize])

# Create a separate scaler for the 'Close' column
scaler_close = MinMaxScaler()
scaler_close.fit(data[['Close']])

# Step 2: Splitting the Data
train_data = data.iloc[:501]  # Select data from 0 to 500 for training

# Step 3: Preparing the Data for LSTM
sequence_length = 20

def create_sequences(X, y, sequence_length):
    X_sequences, y_sequences = [], []
    for i in range(len(X) - sequence_length + 1):
        X_sequences.append(X[i:i+sequence_length])
        y_sequences.append(y[i:i+sequence_length-1])
    return np.array(X_sequences), np.array(y_sequences)

X_train, y_train = create_sequences(train_data[columns_to_normalize], train_data['Close'], sequence_length)

# Reshape the data for LSTM input shape (samples, time steps, features)
X_train = np.reshape(X_train, (X_train.shape[0], sequence_length, len(columns_to_normalize)))

# Step 4: Defining the LSTM Model
model = Sequential()
model.add(LSTM(50, input_shape=(sequence_length, len(columns_to_normalize))))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# Step 5: Training the LSTM Model
model.fit(X_train, y_train, epochs=10, batch_size=32)


# Save the trained model
model.save('C:/Users/imale/Documents/Projects/sbx/sbx/model.h5')

 
