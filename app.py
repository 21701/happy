import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from eda_app import run_eda_app
from ml_app import run_ml_app




def main() :
    st.title('World Happiness Report')


    # 사이드바 메뉴 
    st.sidebar.title('World Happiness Report')

    menu = ['Home','EDA','Machine learning']
    choice = st.sidebar.selectbox('MENU',menu)
    
    if choice == 'Home':
       
        st.header('Happiness scored according to economic production, social support, etc.')
        st.subheader('\n')
        st.subheader('- Data Columns Information')
        df = pd.read_csv('data/happy.csv',index_col=0)
        st.dataframe(df)
        
        st.write('* Country : Name of the country.')
        st.write('* Happiness Rank : Rank of the country based on the Happiness Score.')
        st.write('* Happiness Score : A metric measured in "How would you rate your happiness on a scale of 0 to 10 where 10 is the happiest."')
        st.write('* Economy (GDP per Capita) : The extent to which GDP contributes to the calculation of the Happiness Score.')
        st.write('* Health (Life Expectancy) : The extent to which Life expectancy contributed to the calculation of the Happiness Score.')
        st.write('* Freedom : The extent to which Freedom contributed to the calculation of the Happiness Score.')
        st.subheader('\n')
        selected_columns = st.multiselect('선택한 컬럼의 정보만 보여줍니다.',df.columns)
        if len(selected_columns) != 0 :
            st.dataframe( df[selected_columns] )
        

        else :
             st.write('선택한 컬럼이 없습니다.')
        

        # selected_column = st.selectbox('컬럼을 선택하세요', df.columns)

        # bins = st.slider('bin의 갯수 조절', min_value=10, max_value=50)

        # fig1 = plt.figure()
        # df[selected_column].hist(bins= bins)
        # st.pyplot(fig1)

        # Country	Happiness Rank	Happiness Score	Economy (GDP per Capita)	Health (Life Expectancy)	Freedom	Generosity
        
        

        
    elif choice == 'EDA':
        run_eda_app()
    elif choice == 'Machine learning':
        run_ml_app()
   
    




if __name__ == '__main__':
    main()