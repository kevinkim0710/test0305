import streamlit as st
import time

# 앱의 진행 단계 관리를 위해 session_state 사용
if "step" not in st.session_state:
    st.session_state.step = 1

st.title("나만의 패션 점수 측정기")

if st.session_state.step == 1:
    st.header("1. 신체 정보 입력")
    height = st.selectbox("키를 선택하세요", ["160cm 이하", "161~170cm", "171~180cm", "181cm 이상"])
    weight = st.selectbox("몸무게를 선택하세요", ["50kg 이하", "51~60kg", "61~70kg", "71kg 이상"])
    body_type = st.selectbox("체형을 선택하세요", ["마른편", "보통", "통통"])
    
    if st.button("다음"):
        st.session_state.height = height
        st.session_state.weight = weight
        st.session_state.body_type = body_type
        st.session_state.step = 2
        st.experimental_rerun()

elif st.session_state.step == 2:
    st.header("2. 얼굴 톤 선택")
    face_tone = st.selectbox("당신의 얼굴 톤은?", ["흰편", "중간", "어두운편"])
    
    if st.button("다음"):
        st.session_state.face_tone = face_tone
        st.session_state.step = 3
        st.experimental_rerun()

elif st.session_state.step == 3:
    # 이미지 선택 단계 - 3회 반복
    if "image_step" not in st.session_state:
        st.session_state.image_step = 1
        st.session_state.selected_images = []
    
    st.header(f"3. 패션 이미지 선택 ({st.session_state.image_step} / 3)")
    
    # 예시 이미지 URL (플레이스홀더 이미지 사용)
    images = [
        "https://via.placeholder.com/150?text=Image1",
        "https://via.placeholder.com/150?text=Image2",
        "https://via.placeholder.com/150?text=Image3"
    ]
    
    selected = None
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            st.image(images[i])
            if st.button("이 이미지 선택", key=f"img_{st.session_state.image_step}_{i}"):
                selected = images[i]
    
    if selected is not None:
        st.session_state.selected_images.append(selected)
        st.session_state.image_step += 1
        if st.session_state.image_step > 3:
            st.session_state.step = 4
        st.experimental_rerun()

elif st.session_state.step == 4:
    st.header("4. 결과 분석 중...")
    # 5초간 진행바 표시
    progress_bar = st.progress(0)
    for percent in range(101):
        time.sleep(0.05)  # 0.05초 * 100 = 5초
        progress_bar.progress(percent)
    st.session_state.step = 5
    st.experimental_rerun()

elif st.session_state.step == 5:
    st.header("당신의 패션 점수는?!")
    st.subheader("24점!")
    # 축하 효과 - balloons
    st.balloons()
