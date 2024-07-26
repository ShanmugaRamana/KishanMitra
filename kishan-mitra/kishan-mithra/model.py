import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
data = pd.read_csv("TARP.csv")

soil_moisture = data["Soil Moisture"]
temp = data["Temperature"]
soil_humidity = data[" Soil Humidity"]
status = data["Status"]
x = [[soil_moisture[i], temp[i], soil_humidity[i]] for i in range(len(soil_moisture))]
X = np.array(x)
y=[]
for i in range(len(status)):
    if(status[i] == "ON"):
        y.append(1)
    else:
        y.append(0)
y = np.array(y)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_norm = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)
model = Sequential()
model.add(Dense(units = 10,activation = "relu"))
model.add(Dense(units = 5,activation ="relu"))
model.add(Dense(units =1,activation ="sigmoid"))
model.compile(loss = BinaryCrossentropy(), optimizer = Adam())
model.fit(X_norm,y_train,epochs = 100)
y_hat = model.predict(X_test)
y_pred_discrete = (y_hat > 0.5).astype(int)

model.save('kishanmithra-model.h5')  # Save the model

