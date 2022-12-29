import streamlit as st
import pandas as pd
import numpy as np

st.markdown("""
<style>
tr {
    font-size:1.6em !important;
}

* {
    font-family: serif !important;
}
</style>
""", unsafe_allow_html=True)

def top():
    st.title('Important 800 words for H.S.std.')
    st.header('from Arcsecond / Elsy')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random_all/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)


def page01():
    st.title('Page01')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random1/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page02():
    st.title('Page02')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random2/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page03():
    st.title('Page03')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random3/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page04():
    st.title('Page04')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random4/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page05():
    st.title('Page05')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random5/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page06():
    st.title('Page06')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random6/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page07():
    st.title('Page07')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random7/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page08():
    st.title('Page08')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random8/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page09():
    st.title('Page09')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random9/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page10():
    st.title('Page10')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random10/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page11():
    st.title('Page11')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random11/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page12():
    st.title('Page12')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random12/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page13():
    st.title('Page13')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random13/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page14():
    st.title('Page14')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random14/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page15():
    st.title('Page15')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random15/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page16():
    st.title('Page16')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random16/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

def page17():
    st.title('Page17')
    rand = np.random.randint(1, 10)
    st.header("random_seed : " + str(rand))
    df = pd.read_csv('R/random17/Er_' + str(rand) + '.csv',encoding='UTF-8')
    st.markdown(df.to_markdown(), unsafe_allow_html=True)

pages = dict(
    top="Top_Page",
    page01="page01 : 001-050",
    page02="page02 : 051-100",
    page03="page03 : 101-150",
    page04="page04 : 151-200",
    page05="page05 : 201-250",
    page06="page06 : 251-300",
    page07="page07 : 301-350",
    page08="page08 : 351-400",
    page09="page09 : 401-450",
    page10="page10 : 451-500",
    page11="page11 : 501-550",
    page12="page12 : 551-600",
    page13="page13 : 601-650",
    page14="page14 : 651-700",
    page15="page15 : 701-750",
    page16="page16 : 751-800",
    page17="page17 : 801-842",
)

page_id = st.sidebar.selectbox( # st.sidebar.*でサイドバーに表示する
    "Select",
    ["top", "page01", "page02", "page03", "page04", "page05",
            "page06", "page07", "page08", "page09", "page10",
            "page11", "page12", "page13", "page14", "page15",
            "page16", "page17"],
    format_func=lambda page_id: pages[page_id],
)

if page_id == "top":
    top()

if page_id == "page01":
    page01()

if page_id == "page02":
    page02()

if page_id == "page03":
    page03()

if page_id == "page04":
    page04()

if page_id == "page05":
    page05()

if page_id == "page06":
    page06()

if page_id == "page07":
    page07()

if page_id == "page08":
    page08()

if page_id == "page09":
    page09()

if page_id == "page10":
    page10()

if page_id == "page11":
    page11()

if page_id == "page12":
    page12()

if page_id == "page13":
    page13()

if page_id == "page14":
    page14()

if page_id == "page15":
    page15()

if page_id == "page16":
    page16()

if page_id == "page17":
    page17()
