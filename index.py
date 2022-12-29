import streamlit as st
import pandas as pd

st.title('Important 800 words for H.S.std.')
st.header('from Arcsecond / Elsy')

st.markdown("""
<style>
.big-font {
    font-size:2.5em !important;
}
</style>
""", unsafe_allow_html=True)


df = pd.read_csv('R/random_all/Er_1.csv',encoding='UTF-8')

# st.markdown('<p class = "big-font"> df.to_markdown() </p>', unsafe_allow_html=True)

st.markdown("[prob1](./problem.py)", unsafe_allow_html=True)
st.markdown(df.to_markdown(), unsafe_allow_html=True)