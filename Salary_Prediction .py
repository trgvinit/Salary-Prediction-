#loading data
import pandas as pd

df = pd.read_csv('/content/Salary Data.csv')
df.head()

#to remove missing values
df.isnull().sum()
df.dropna(inplace=True)
df.isnull().sum()

#to separate categorical and numerical columns
df.info()
cat_cols = df.select_dtypes(include=['object']).columns

#Encoding 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in cat_cols:
  df[col] = le.fit_transform(df[col])

#deciding target 
x = df.drop(columns=['Salary'])
y = df['Salary']

#splitting
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#standerdization
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#training model
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train,y_train)

#prediction
y_pred = model.predict(x_test)

#evaluation
from sklearn.metrics import r2_score

accuracy = r2_score(y_test,y_pred)
print(accuracy*100)
import numpy as np
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
print(mape)