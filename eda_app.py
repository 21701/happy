import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app():


    df = pd.read_csv('data/happy.csv',index_col=0)
    st.subheader('EDA')
    
     # 컬럼을 선택하면 해당 컬럼들만 데이터프레임 표시하는 화면
    selected_columns = st.multiselect('Only the information of the selected columns is displayed.',df.columns)
    if len(selected_columns) != 0  :
        st.dataframe( df[selected_columns] )
    else :
        st.dataframe(df)
        # st.write('< 선택한 컬럼 표시 >')
    check = st.checkbox('Statistics')

    if check :
        st.dataframe(df.describe())
    
    
    # 라디오버튼
    
    radio_menu = ['DataFrame','Statistics']
    selected_radio = st.radio('Select',radio_menu)
    if selected_radio == 'DataFrame':
        st.dataframe(df)
    elif selected_radio == 'Statistics':
        st.dataframe(df.describe())

    st.subheader('\n')

    
   

    st.subheader('\n')


    
    st.sidebar.subheader('최고 행복 순위')
    word = st.sidebar.text_input('국가명 검색')
    # 검색을 위해서 소문자로 만든다.
    word = word.lower() 
    # 2. 검색어를 데이터프레임의 Customer Name 컬럼에서 검색해서 가져온다.
    df_search = df.loc[ df['Country'].str.lower().str.contains(word) ,  ]
    print(df_search.iloc[:1,:1+1])
    btn= st.sidebar.button('검색')
    if btn:
        st.sidebar.dataframe(df_search.iloc[:1,:1+1].head(1))
        st.sidebar.write('" {}의 최고 순위는 {}위 입니다. "'.format(df_search['Country'].values[0],df_search['Happiness Rank'].values[0]))
    else : st.write('검색어를 입력하면 순위가 나옵니다')



  # # 고객의 이름을 검색할 수 있는 기능 개발
    # # 1. 유저한테 검색어 입력을 받습니다.
    # st.subheader('\n')
    # st.subheader('나라를 검색하면 해당정보를 알려드립니다')

    # word = st.text_input('검색어를 입력하세요')
    # # 검색을 위해서 소문자로 만든다.
    # word = word.lower() 
    # # 2. 검색어를 데이터프레임의 Customer Name 컬럼에서 검색해서 가져온다.
    # # print(word)
    
    # df_search = df.loc[ df['Country'].str.lower().str.contains(word) ,  ]
    # st.dataframe(df_search)

    
    





    # 유저가 컬럼을 선택하면,
    # 해당 컬럼의 min과 max에 해당하는 사람이 누구인지
    # 그사람의 데이터를 화면에 보여주는 기능 개발

    #### 문자열 데이터가 아닌, 컬럼들만 가져오는 코드 ###
    # print(df.columns)
    # print(df.dtypes != object)
    # print( df.columns[df.dtypes != object])
    


    st.subheader('\n')

    st.subheader('선택한 컬럼의 최소값, 최대값 정보')
    number_columns = df.columns[df.dtypes != object]

    selected_minmax_column = st.selectbox('컬럼 선택',number_columns)
    
    # # 선택한 컬럼의 최소값에 해당되는 사람의 데이터 출력
    df[selected_minmax_column] == df[selected_minmax_column].min()
    min_data = df.loc[df[selected_minmax_column] == df[selected_minmax_column].min(),]
    st.dataframe(min_data)


    # # 선택한 컬럼의 최대값에 해당되는 사람의 데이터 출력
    max_data = df.loc[df[selected_minmax_column] == df[selected_minmax_column].max(),]
    st.dataframe(max_data)

    
    
    

    # # 고객의 이름을 검색할 수 있는 기능 개발
    # # 1. 유저한테 검색어 입력을 받습니다.
    # st.subheader('\n')
    # st.subheader('나라를 검색하면 해당정보를 알려드립니다')

    # word = st.text_input('검색어를 입력하세요')
    # # 검색을 위해서 소문자로 만든다.
    # word = word.lower() 
    # # 2. 검색어를 데이터프레임의 Customer Name 컬럼에서 검색해서 가져온다.
    # # print(word)
    
    # df_search = df.loc[ df['Country'].str.lower().str.contains(word) ,  ]
    # st.dataframe(df_search)


    # 3. 화면에 결과를 보여준다.
    
    # 상관관계 분석을 위한, 상관계수 보여주는 화면 개발
    st.subheader('\n')
    st.subheader('상관계수')
    # st.dataframe(df.corr())
    
    df_corr = df.iloc[:, 3: ]
    selected_corr = st.multiselect('상관계수 컬럼을 선택하면 수치, 차트로 표시',df_corr.columns)
    
    # 유저가 1개라도 컬럼을 선택했을 경우
    if len(selected_corr) > 0 :
        st.dataframe(df_corr[selected_corr].corr())

        # 상관계수를 수치로도 구하고, 차트로도 표시하라.
        
        fig = sns.pairplot(data=df_corr[selected_corr] )
        st.pyplot(fig)
    # 유저가 컬럼을 선택하지 않은 경우
    else :
        st.write('선택한 컬럼이 없습니다.')

    # fig1 = plt.figure()
    # plt.figure(figsize=(10,8))
    # sns.heatmap(data=df, cmap='RdPu', annot=True, fmt='.1f', linewidths=0.8 )
    # st.pyplot(fig1)

