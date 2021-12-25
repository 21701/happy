import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

def run_eda_app2():

    df = pd.read_csv('data/happy.csv',index_col=0)
    word = st.sidebar.text_input('국가명 검색')
    # 검색을 위해서 소문자로 만든다.
    word = word.lower() 
    # 2. 검색어를 데이터프레임의 Customer Name 컬럼에서 검색해서 가져온다.
    df_search = df.loc[ df['Country'].str.lower().str.contains(word) ,  ]

    st.sidebar.dataframe(df_search.iloc[:,:1+1].head())