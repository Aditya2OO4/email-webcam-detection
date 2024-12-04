import cv2
import streamlit as st
from time import strftime

st.title("Motion Detection")
start = st.button("Start Camera")

if start:

    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=strftime("%A"), org = (50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=strftime("%H:%M:%S"), org=(50, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

