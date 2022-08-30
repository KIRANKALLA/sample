import streamlit as st
import pandas as pd
st.title('MY FIRST APP')
data=pd.read_excel('hdp.xlsx')
st.dataframe(data)
