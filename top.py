import streamlit as st
import pandas as pd

# st.set_page_config(layout="wide")

df = pd.read_csv('R/random1/Er_10.csv',encoding='UTF-8')

st.title('Important 800 words for H.S.std.')
st.header('from Arcsecond / Elsy')

st.markdown("""
<style>
.big-font {
    font-size:2.5em !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(df.to_markdown(), unsafe_allow_html=True)