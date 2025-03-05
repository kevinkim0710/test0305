import streamlit as st
import time
import random

# 버튼 클릭 시 호출할 공통 콜백 함수
def go_to_step(new_step, **kwargs):
    for key, value in kwargs.items():
        st.session_state[key] = value
    st.session_state.step = new_step

# 이미지 선택 버튼 클릭 시 호출할 콜백 함수
def select_image(image, next_step):
    if "selected_images" not in st.session_state:
        st.session_state.selected_images = []
    st.session_state.selected_images.append(image)
    st.session_state.step = next_step

# 초기 상태 설정
if "step" not in st.session_state:
    st.session_state.step = 1

st.title("나만의 패션 점수 측정기")

if st.session_state.step == 1:
    # Step 1: 신체 정보 입력
    st.header("1. 신체 정보 입력")
    height = st.selectbox("키를 선택하세요", ["160cm 이하", "161~170cm", "171~180cm", "181cm 이상"])
    weight = st.selectbox("몸무게를 선택하세요", ["50kg 이하", "51~60kg", "61~70kg", "71kg 이상"])
    body_type = st.selectbox("체형을 선택하세요", ["마른편", "보통", "통통"])
    st.button("다음", key="btn1", on_click=go_to_step, args=(2,), 
              kwargs={"height": height, "weight": weight, "body_type": body_type})

elif st.session_state.step == 2:
    # Step 2: 얼굴 톤 선택
    st.header("2. 얼굴 톤 선택")
    face_tone = st.selectbox("당신의 얼굴 톤은?", ["흰편", "중간", "어두운편"])
    st.button("다음", key="btn2", on_click=go_to_step, args=(3,), 
              kwargs={"face_tone": face_tone})

elif st.session_state.step == 3:
    # Step 3: 첫번째 이미지 선택
    st.header("3-1. 패션 이미지 선택 (1/3)")
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
    # 매 스텝마다 3개의 이미지 중 랜덤 선택
    current_images = random.sample(images, 3)
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            st.image(current_images[i])
            st.button("이 이미지 선택", key=f"step3_img{i}", on_click=select_image, args=(current_images[i], 4))

elif st.session_state.step == 4:
    # Step 4: 두번째 이미지 선택
    st.header("3-2. 패션 이미지 선택 (2/3)")
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
    current_images = random.sample(images, 3)
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            st.image(current_images[i])
            st.button("이 이미지 선택", key=f"step4_img{i}", on_click=select_image, args=(current_images[i], 5))

elif st.session_state.step == 5:
    # Step 5: 세번째 이미지 선택
    st.header("3-3. 패션 이미지 선택 (3/3)")
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
    current_images = random.sample(images, 3)
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            st.image(current_images[i])
            st.button("이 이미지 선택", key=f"step5_img{i}", on_click=select_image, args=(current_images[i], 6))

elif st.session_state.step == 6:
    # Step 6: 결과 분석 로딩
    st.header("4. 결과 분석 중...")
    progress_bar = st.progress(0)
    for percent in range(101):
        time.sleep(0.05)
        progress_bar.progress(percent)
    st.button("결과 보기", key="result", on_click=go_to_step, args=(7,))

elif st.session_state.step == 7:
    st.header("당신의 패션 점수는?!")
    st.header("24점! 진짜 최악이네요!")
    st.header("어울리는 스타일 찾으러가기 👇")
    st.header("https://4910.kr/codi")
    st.balloons()
