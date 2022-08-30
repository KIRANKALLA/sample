import streamlit as st
st.title('MY FIRST APP')
data=pd.read_excel('hdp.xlsx')
st.dataframe(data)
