import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
d1=pd.read_csv('housing_price_dataset.csv')
#d1
#d1.columns
x=d1.iloc[:,:-1].values
#x
y=d1.iloc[:,-1].values
#y
l=LabelEncoder()
x[:,3]=l.fit_transform(x[:,3])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
r=LinearRegression()
r.fit(x_train,y_train)
#x=r.predict([[2000,3,4,1,1000]])
#x
st.header('House Price Prediction')
sqft=st.number_input("Enter sqft")
bed=st.number_input("Enter nof beds")
bath=st.number_input("Enter nof bathrooms")
nei=st.selectbox("select options",options=['Rural','Urban','Sub-Urban'])
if(nei=="Rural"):
    nei=0
elif(nei=="Sub-Urban"):
    nei=1
elif(nei=="Urban"):
    nei=2
year=st.number_input('Enter year')
if(st.button("predict")):
    data=[[sqft,bed,bath,nei,year]]
    value=r.predict(data)
    st.success("your price is:"+str(value))