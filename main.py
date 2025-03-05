import streamlit as st
import time
import random

def go_to_step(new_step, **kwargs):
    for key, value in kwargs.items():
        st.session_state[key] = value
    st.session_state.step = new_step

if "step" not in st.session_state:
    st.session_state.step = 1

st.title("나만의 패션 점수 측정기")

if st.session_state.step == 1:
    st.header("1. 신체 정보 입력")
    height = st.selectbox("키를 선택하세요", ["160cm 이하", "161~170cm", "171~180cm", "181cm 이상"])
    weight = st.selectbox("몸무게를 선택하세요", ["50kg 이하", "51~60kg", "61~70kg", "71kg 이상"])
    body_type = st.selectbox("체형을 선택하세요", ["마른편", "보통", "통통"])
    
    st.button("다음", key="btn1", on_click=go_to_step, args=(2,), kwargs={"height": height, "weight": weight, "body_type": body_type})

elif st.session_state.step == 2:
    st.header("2. 얼굴 톤 선택")
    face_tone = st.selectbox("당신의 얼굴 톤은?", ["흰편", "중간", "어두운편"])
    
    st.button("다음", key="btn2", on_click=go_to_step, args=(3,), kwargs={"face_tone": face_tone})

elif st.session_state.step == 3:
    # 이미지 선택 단계 (총 3회)
    if "image_step" not in st.session_state:
        st.session_state.image_step = 1
        st.session_state.selected_images = []

    st.header(f"3. 패션 이미지 선택 ({st.session_state.image_step} / 3)")
    
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
    
    # 매 단계마다 3개의 랜덤 이미지 생성 (한 번 생성된 경우 그대로 유지)
    if "current_images" not in st.session_state or st.session_state.get("last_image_step") != st.session_state.image_step:
        st.session_state.current_images = random.sample(images, 3)
        st.session_state.last_image_step = st.session_state.image_step

    selected_flag = False
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            st.image(st.session_state.current_images[i])
            if st.button("이 이미지 선택", key=f"img_{st.session_state.image_step}_{i}"):
                st.session_state.selected_images.append(st.session_state.current_images[i])
                st.session_state.image_step += 1
                if st.session_state.image_step > 3:
                    st.session_state.step = 4
                selected_flag = True
    if selected_flag:
        st.experimental_rerun()

elif st.session_state.step == 4:
    st.header("4. 결과 분석 중...")
    progress_bar = st.progress(0)
    for percent in range(101):
        time.sleep(0.05)
        progress_bar.progress(percent)
    st.button("결과 보기", key="result", on_click=go_to_step, args=(5,))

elif st.session_state.step == 5:
    st.header("당신의 패션 점수는?!")
    st.subheader("24점! 진짜 최악이네요!")
    st.subheader("어울리는 스타일 찾으러가기 👇")
    st.subheader("https://4910.kr/codi")
    st.balloons()
