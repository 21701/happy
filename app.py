import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle

from eda_app import run_eda_app
from ml_app import run_ml_app

def main() :
    st.title('세계 행복 보고서')

    # 사이드바 메뉴 
    menu = ['Home','EDA','ML']
    choice = st.sidebar.selectbox('메뉴',menu)
    
    if choice == 'Home':
        st.write('경제적 생산, 사회적 지지 등에 따라 점수를 매긴 행복지수')
        st.write('왼쪽의 사이드바에서 선택하세요.')
    elif choice == 'EDA':
        run_eda_app()
    elif choice == 'ML':
        run_ml_app()




if __name__ == '__main__':
    main()