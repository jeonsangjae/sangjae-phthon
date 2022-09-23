import streamlit as st
import pandas as pd

# 메인페이지 
# Iris 사진 나타하기 - https://ouellette001.com/PapiersPeints/images/Iris_versicolor_0021_1280.jpg
# https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv 읽고 나타내기 
def main_page():
    st.title('나를 소개합니다!!')
    st.header('Aivler 전상재를 알아봅시다')
    
    me = st.radio( '어떤 점이 궁금하신가요?',('나이', '사는 곳', '생일'))
    if me == '나이':
        st.write('28살 입니다🐷') 
    elif me == '사는 곳':
        st.write('경상남도 진주입니다.') 
    else:
        st.write('🎂10월 15일 입니다.🎂') 
    
    agree = st.checkbox('사진')
    if agree:
        st.image('/Users/User/streamlit/friends/me.jpg',caption = '할로윈 파티',width = 300)
    
# 2페이지: 세 개의 columns으로 나누어 꽃 이름과 사진 나타내기
def page2():
    st.header('취미 생활')
    tab1, tab2, tab3 = st.tabs(['기타 치기','피아노 치기','노래 부르기']) 
    with tab1:
        st.text('기본적인 것밖에 못 치지만 좋아합니다 ❤')
        st.text('한번 들어 보시죠!!')
        st.text('자전거 탄 풍경 - 나에게 넌 너에게 난')
        st.image('/Users/User/streamlit/friends/guitar.jpg',caption = '기타 치는 나',width = 300)
        st.audio('/Users/User/streamlit/friends/guitar.m4a')
    with tab2:
        st.text('제가 직접 친 곡이랍니다!!!')
        st.text('피아노 소리 한 번 들어보시죠~!')
        st.text('이루마의 river flow in you 🎹')
        st.audio('/Users/User/streamlit/friends/piano.m4a')
    with tab3:
        st.text('쑥스럽지만 제 친구와 함께 공연했던 영상입니다ㅎㅎ')
        st.text('한동근,최효인 - 스물다섯 스물하나 🎤')
        st.video('/Users/User/streamlit/friends/sing.mp4')


# 3페이지: 세 개의 tab을 사용하여 iris 3가지 꽃 나타내기
def page3():
    st.header('친구 관계')
    tab1, tab2, tab3 = st.tabs(['고등학교 친구','대학교 친구','Aivle 친구'])

    with tab1:
        st.text('고등학교 친구')
        st.image('/Users/User/streamlit/friends/highschool.jpg',caption = '고등학교 친구들과', width = 400)
    with tab2:
        st.text('대학교 친구')
        st.image('/Users/User/streamlit/friends/univercity.jpg',caption = '대학교 친구들과', width = 400)
    with tab3:
        st.text('Aivle 친구')
        st.image('https://github.com/jeonsangjae/kt-aivle/blob/master/friends/aivle.jpg',caption = 'Aivle 친구들과 한컷', width = 400)

        
# 딕셔너리 선언 {  ‘selectbox항목’ : 페이지명 …  }
page_names_to_funcs = {'나를 소개합니다': main_page, '나의 취미생활': page2, '나의 친구들': page3}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('페이지 선택',page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\me.py