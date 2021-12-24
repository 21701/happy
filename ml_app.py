import streamlit as st
import pandas as pd
import numpy as np
import joblib


def run_ml_app():
    st.subheader('Machine Learning')
    st.subheader('\n')

    # 1. 유저한테, 데이터를 입력받습니다.
    rank = st.number_input('Happiness Rank : Rank of the country based on the Happiness Score1.',min_value=1,max_value=158)
    st.write('\n')
  
    gdp_slider = st.slider('Economy (GDP per Capita) : The extent to which GDP contributes to the calculation of the Happiness Score.',min_value=0.0,max_value=2.1)
    gdp = gdp_slider
    st.write('\n')

    health_slider = st.slider('Health (Life Expectancy) : The extent to which Life expectancy contributed to the calculation of the Happiness Score.',min_value=0.0,max_value=1.2)
    health = health_slider
    st.write('\n')

    freedom_slider = st.slider('Freedom : The extent to which Freedom contributed to the calculation of the Happiness Score.',min_value=0.0,max_value=1.2)
    freedom = freedom_slider
    st.write('\n')

    generosity_slider = st.slider('Generosity',min_value=0.0,max_value=1.0)
    generosity = generosity_slider
    st.write('\n')
    
    # gender = st.radio('성별을 입력하세요.',['남자','여자'])
    # if gender == '남자' :
    #     gender_number = 1
    # elif gender == '여자' :
    #     gender_number = 0

    # df = pd.read_csv('data/Car_Purchasing_Data.csv')

    # age = st.number_input('나이 입력',min_value=1,max_value=120)
    # salary = st.number_input('연봉 입력',min_value=10000 )
    # debt = st.number_input('카드 빚 입력', min_value=0)
    # worth = st.number_input('자산 입력',min_value=10000)
    # print(debt)
    
    # 2. 모델에 예측한다.
    # 2-1 신규데이터를 넘파이로 만든다.
    new_data = np.array([rank,gdp,health,freedom,generosity])
    new_data = new_data.reshape(1,5)

    # 2-2 스케일러와 인공지능을 변수로 불러온다
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')
    regressor = joblib.load('data/regressor.pkl')

    # 2-3 신규 데이터를 피쳐스케일링 한다.
    new_data = scaler_X.transform(new_data)
    # 2-4 인공지능에게 예측을 하게 한다.
    y_pred = regressor.predict(new_data)

    # 2-5 예측한 결과는, 다시 원래대로 복구해 줘야 한다.
    print(y_pred)

    y_pred = scaler_y.inverse_transform(y_pred.reshape(1,1))
    print(y_pred)
    
    # 3. 예측 결과를 웹 대시보드에 표시한다.

    btn = st.button('예측 결과 보기')
    # 결과가 소수점으로 나오는데,소수점 뒤 한자리까지만 나오도록
    # 코드 수정하세요
    y_pred = y_pred.round()

    if btn :
        st.write('< 예측 결과 > " 당신의 행복 지수는 {} 입니다. " '.format(y_pred[0,0]))