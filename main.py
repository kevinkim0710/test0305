import streamlit as st
import time
import random

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
        st.stop()  # 실행 중단 후 다음 상호작용에서 업데이트된 상태 반영

elif st.session_state.step == 2:
    st.header("2. 얼굴 톤 선택")
    face_tone = st.selectbox("당신의 얼굴 톤은?", ["흰편", "중간", "어두운편"])
    
    if st.button("다음"):
        st.session_state.face_tone = face_tone
        st.session_state.step = 3
        st.stop()

elif st.session_state.step == 3:
    # 이미지 선택 단계 - 3회 반복
    if "image_step" not in st.session_state:
        st.session_state.image_step = 1
        st.session_state.selected_images = []
    
    st.header(f"3. 패션 이미지 선택 ({st.session_state.image_step} / 3)")
    
    # 예시 이미지 URL 리스트
    images = [
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_49_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_48_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_47_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_46_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_45_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_44_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_43_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_42_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/1_41_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/3_30_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/3_29_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/3_28_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/3_27_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/3_26_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/3_25_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/3_24_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/2_30_a_1.webp",
        "https://img.a-bly.com/4910/data/style_codis/images/curation/2_29_a_1.webp"
    ]
    
    # 매 이미지 선택 단계마다 랜덤하게 3개의 이미지를 선택 (같은 단계 내에서는 동일하게 유지)
    if "current_images" not in st.session_state or st.session_state.get("last_image_step") != st.session_state.image_step:
        st.session_state.current_images = random.sample(images, 3)
        st.session_state.last_image_step = st.session_state.image_step

    selected = None
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            st.image(st.session_state.current_images[i])
            if st.button("이 이미지 선택", key=f"img_{st.session_state.image_step}_{i}"):
                selected = st.session_state.current_images[i]
    
    if selected is not None:
        st.session_state.selected_images.append(selected)
        st.session_state.image_step += 1
        # 다음 단계에 대비해 랜덤 이미지셋 삭제
        if "current_images" in st.session_state:
            del st.session_state.current_images
        if st.session_state.image_step > 3:
            st.session_state.step = 4
        st.stop()

elif st.session_state.step == 4:
    st.header("4. 결과 분석 중...")
    progress_bar = st.progress(0)
    for percent in range(101):
        time.sleep(0.05)  # 0.05초 * 100 = 5초
        progress_bar.progress(percent)
    # 5초 로딩 후 결과 보기 버튼 추가
    if st.button("결과 보기"):
        st.session_state.step = 5
        st.stop()

elif st.session_state.step == 5:
    st.header("당신의 패션 점수는?!")
    st.subheader("24점!")
    st.balloons()
