import streamlit as st
import pandas as pd
st.title('MY FIRST APP')
data=pd.read_csv('loan_data.csv')
st.dataframe(data)
