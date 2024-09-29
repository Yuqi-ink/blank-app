import streamlit as st
import streamlit_survey as ss

st.title("🎈 User Feedback Survey")
st.write(
    "Please watch the following videos and select the one you find most satisfactory for each question. 请观看视频并根据问题选择你认为最好的视频。"
)

survey = ss.StreamlitSurvey()

st.title("Q0 问题0")
st.write(
    "Source video is on the left, others are results numbered from A to E. Please choose the video for every question according to the editing task. Recommend to use the zoom in button."
)
st.write(
    "最左边是原视频，右边为编号从A到E的编辑结果，请根据编辑任务为每个问题选择视频.推荐点击放大观看按钮进行观看"
)
st.write(
    "The editing task (编辑任务是): \"A girl wearing necklace. 给女孩戴上项链.\""
)

st.video("test1.mp4")

survey.radio("Which video best preserves the motion of the original video? 哪个视频最好地保持了原视频的运动轨迹?", options=["A","B","C","D","E","F"], id="Q01")

survey.radio("Which video has the best editing quality? 哪个视频编辑效果最好?", options=["A","B","C","D","E","F"], id="Q02")

survey.radio("Which video keep the best temporal consistency? 哪个视频的帧间连贯性保持得最好?", options=["A","B","C","D","E","F"], id="Q03")

st.title("Q1 问题1")

st.video("test2.mp4")

survey.radio("Which video best preserves the motion of the original video? 哪个视频最好地保持了原视频的运动轨迹?", options=["A","B","C","D","E","F"], id="Q11")

survey.radio("Which video has the best editing quality? 哪个视频编辑效果最好?", options=["A","B","C","D","E","F"], id="Q12")

survey.radio("Which video keep the best temporal consistency? 哪个视频的帧间连贯性保持得最好?", options=["A","B","C","D","E","F"], id="Q13")

json = survey.to_json()

submit = st.button(label="📑 Submit", type="primary", use_container_width=True)

if submit:
    st.success("Thank you for participating! 感谢您的参与！")