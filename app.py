import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
from eda_app import run_eda_app
from ml_app import run_ml_app

[theme]
base="dark"
primaryColor="#523030"
secondaryBackgroundColor="#5e659e"
textColor="#c15252"



def main() :
    st.title('World Happiness Report')


    # 사이드바 메뉴 
    st.sidebar.title('World Happiness Report')

    menu = ['Home','EDA','Machine learning']
    choice = st.sidebar.selectbox('MENU',menu)
    
    if choice == 'Home':
        st.write('Happiness scored according to economic production, social support, etc.')
        st.write ('\n')
        st.write('데이터 설명')
        st.write('* Country : Name of the country.')
        st.write('* Happiness Rank : Rank of the country based on the Happiness Score.')
        st.write('* Happiness Score : A metric measured in "How would you rate your happiness on a scale of 0 to 10 where 10 is the happiest."')

        
        
    elif choice == 'EDA':
        run_eda_app()
    elif choice == 'Machine learning':
        run_ml_app()
   
    




if __name__ == '__main__':
    main()