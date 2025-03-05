import streamlit as st
import time
import random

if "step" not in st.session_state:
    st.session_state.step = 1

st.title("나만의 패션 점수 측정기")

if st.session_state.step == 1:
    st.header("1. 신체 정보 입력")
    height = st.selectbox("키를 선택하세요", ["160cm 이하", "161~170cm", "171~180cm", "181cm 이상"])
    weight = st.selectbox("몸무게를 선택하세요", ["50kg 이하", "51~60kg", "61~70kg", "71kg 이상"])
    body_type = st.selectbox("체형을 선택하세요", ["마른편", "보통", "통통"])
    
    if st.button("다음", key="btn1"):
        st.session_state.height = height
        st.session_state.weight = weight
        st.session_state.body_type = body_type
        st.session_state.step = 2

elif st.session_state.step == 2:
    st.header("2. 얼굴 톤 선택")
    face_tone = st.selectbox("당신의 얼굴 톤은?", ["흰편", "중간", "어두운편"])
    
    if st.button("다음", key="btn2"):
        st.session_state.face_tone = face_tone
        st.session_state.step = 3

elif st.session_state.step == 3:
    if "image_step" not in st.session_state:
        st.session_state.image_step = 1
        st.session_state.selected_images = []

    st.header(f"3. 패션 이미지 선택 ({st.session_state.image_step} / 3)")
    
    images = [
        # (이미지 URL 리스트 동일)
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_49_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_48_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_47_a_1.webp",
        # ... 나머지 이미지들 ...
        "https://img.a-bly.com/4910/data/style_codis/images/curation/2_29_a_1.webp"
    ]
    
    if "current_images" not in st.session_state or st.session_state.get("last_image_step") != st.session_state.image_step:
        st.session_state.current_images = random.sample(images, 3)
        st.session_state.last_image_step = st.session_state.image_step

    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            st.image(st.session_state.current_images[i])
            if st.button("이 이미지 선택", key=f"img_{st.session_state.image_step}_{i}"):
                st.session_state.selected_images.append(st.session_state.current_images[i])
                st.session_state.image_step += 1
                if st.session_state.image_step > 3:
                    st.session_state.step = 4
                # 여기서는 별도 rerun 호출 없이 상태 업데이트 후, 사용자가 다른 위젯에 상호작용하면 화면이 갱신됩니다.

elif st.session_state.step == 4:
    st.header("4. 결과 분석 중...")
    progress_bar = st.progress(0)
    for percent in range(101):
        time.sleep(0.05)
        progress_bar.progress(percent)
    if st.button("결과 보기", key="result"):
        st.session_state.step = 5

elif st.session_state.step == 5:
    st.header("당신의 패션 점수는?!")
    st.subheader("24점! 진짜 최악이네요!")
    st.subheader("어울리는 스타일 찾으러가기 👇")
    st.subheader("https://4910.kr/codi")
    st.balloons()
