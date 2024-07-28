import streamlit as st
import time as ts
import pyautogui as autogui
import data


st.markdown("""
<style>
.st-emotion-cache-h4xjwg.ezrtsby2
{
    visibility:hidden
}
</style>
""", unsafe_allow_html=True)

    #autogui.hotkey("ctrl","F5")


@st.cache_data(show_spinner=False)
def pro_bar_email():
    bar = st.progress(0)
    progress_status = st.empty()
    for i in range(100):
        value = (i + 1)
        bar.progress(value)
        progress_status.write(str(i + 1) + "%")
        ts.sleep(0.20)

@st.cache_data(show_spinner=False)
def pro_bar_sms():
    bar = st.progress(0)
    progress_status = st.empty()
    for i in range(100):
        value = (i + 1)
        bar.progress(value)
        progress_status.write(str(i + 1) + "%")
        ts.sleep(0.20)

email_text="Code will be shown here"
sms_text="Code will be shown here"



if "email_clicked" not in st.session_state:
    st.session_state.email_clicked = False


if "sms_clicked" not in st.session_state:
    st.session_state.sms_clicked = False


c1,c2=st.columns([5,3])
c1.header("AIS - Code Scrapper")
message=st.empty()
st.divider()


col1, col2, col3=st.columns([3,1,1])

col3.write("")
col3.write("")

if col3.button("Reset And Try Again"):
    st.cache_data.clear()
    st.session_state.email_clicked = False
    st.session_state.sms_clicked = False
    autogui.hotkey("ctrl", "F5")
    #st.experimental_rerun()


with col1:
    st.caption("Email Verification code:")
    email=st.empty()
    status1 = st.empty()
    btn_email=st.empty()
    sms_cap=st.empty()
    sms=st.empty()
    status2 = st.empty()
    btn_sms=st.empty()


    def create_email_code(text):
        with status1.container():
            pro_bar_email()
        email.code(data.get_email_code())

    def create_sms_code(text):
        with status2.container():
            pro_bar_sms()
        sms.code(data.get_sms_code())


    def email_callback():
        global email_text
        st.session_state.email_clicked = True
        email_text = ""
        create_email_code(email_text)


    def sms_callback():
        global sms_text
        st.session_state.sms_clicked = True
        sms_text = ""
        create_sms_code(sms_text)

    email.code(email_text)
    email_click=btn_email.button("Get Email Code",on_click=email_callback)
    if email_click or st.session_state.email_clicked:
        email_callback()
        btn_email.write("")
        sms.code(sms_text)
        sms_cap.caption("SMS Verification code:")
        sms_click=btn_sms.button("Get SMS Code",on_click=sms_callback)
        if sms_click or st.session_state.sms_clicked:
            sms_callback()
            btn_sms.write("")
            message.success("If Code Were Not Loaded Successfully, Try [Reset And Try Again] Button Or Try Contact Brian O'Conner")














