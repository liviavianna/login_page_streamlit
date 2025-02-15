import streamlit as st
from streamlit import dialog

@st.dialog('Alert')
def login_validation(usr, passw):
    if usr == '' or passw == '':
        st.error('Please enter your username or password.')
    else:
        st.success('Login successful.')
with st.form('sign_in'):
    st.title('Sign In')
    st.caption('Please enter your username and password.')
    st.divider()
    username = st.text_input('Username')
    password = st.text_input('Password',
                             type='password')
    submit_btn = st.form_submit_button(label="Submit",
                                       type="primary",
                                       use_container_width=True)
    google_btn = st.form_submit_button(label="Continue with Google",
                                       type="secondary",
                                       use_container_width=True,
                                       icon=':material/mail:')
    col1, col2, col3, col4 = st.columns(4)
    with col3:
        remember_box = st.checkbox("Remember me")
    with col4:
        forgot_pass = st.html('<p style=margin-top:8px; color:#FFAC41><a href="https://www.google.com.br/?hl=pt-BR">Forgot password?</a></p>')
create_acc_btn = st.button(label="Create an Account",
                           type="secondary",
                           use_container_width=True)
if submit_btn:
    login_validation(username, password)