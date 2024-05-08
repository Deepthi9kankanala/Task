import streamlit as st  
import numpy as np 
import pandas as pd 
import matplotlib.pyplot  as plt 
import plotly.express as px 
def main():
    st.title("charts ex")
    # generate data randomly
data=pd.DataFrame({ 'x' :np.arange(10), 
                         'y' : np.random.randn(10)
                         })
# line chart 
st.subheader("Line chart")
st.line_chart(data['y'])    

# bar chart 
st.subheader("bar chart")
st.bar_chart(data['y']) 

# scattter plot 
st.subheader("scatter chart")
st.scatter_chart(data)  

#plotly 
st.subheader(" plotly ")
p=px.line(data,x='x',y='y',title="Line chart")
st.plotly_chart(p)



if __name__ =="__main__":
    main()