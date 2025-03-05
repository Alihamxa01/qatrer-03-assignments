import streamlit as st
import re

def check_password_strength(password):
    strength = 0

    if len(password) < 8:
        return -1, 0  

    # password requirements
    digit_error = not re.search(r"\d", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if not digit_error:
        strength += 25 
    if not uppercase_error:
        strength += 25  
    if not lowercase_error:
        strength += 20  
    if not special_char_error:
        strength += 30  

    return strength // 25, strength  


st.title("🔒 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, percentage = check_password_strength(password)

    # Length 
    if strength == -1:
        st.error("❌ Your password is too short! Minimum 8 characters required.", icon="⚠️")
    elif strength == 0:
        st.error(f"🚨 Weak Password: You need to improve your password! ({percentage}%)", icon="⚠️")
    elif strength == 1:
        st.warning(f"🟠 Medium Strength: It's okay, but you need more security! ({percentage}%)", icon="⚡")
    else:
        st.success(f"✅ Strong Password: Great! Your password is secure! ({percentage}%)", icon="🔐")

    #  color percentage
    if percentage <= 40:
        color = "red"
    elif percentage <= 70:
        color = "yellow"
    else:
        color = "green"

    # Progress Bar
    st.markdown(
        f"""
        <div style="
            width: 100%;
            height: 20px;
            background-color: lightgray;
            border-radius: 10px;
            position: relative;">
            <div style="
                width: {percentage}%;
                height: 100%;
                background-color: {color};
                border-radius: 10px;">
            </div>
        </div>
        <p style="text-align:center; font-size:18px; font-weight:bold; color:{color};">
            {percentage}% Secure
        </p>
        """,
        unsafe_allow_html=True
    )

 
    st.write("### 🔍 Password Analysis:")
    st.write(f"- 🔢 Contains Number: {'✅' if re.search(r'\d', password) else '❌'}")
    st.write(f"- 🔠 Contains Uppercase Letter: {'✅' if re.search(r'[A-Z]', password) else '❌'}")
    st.write(f"- 🔡 Contains Lowercase Letter: {'✅' if re.search(r'[a-z]', password) else '❌'}")
    st.write(f"- 🔣 Contains Special Character: {'✅' if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password) else '❌'}")
    st.write(f"- 📏 Length: **{len(password)} characters** (Minimum 8 recommended)")

st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:16px; font-weight:bold; color:#b3b6b7;'>✨ Made by Ali Hamza ✨</p>",
    unsafe_allow_html=True
)
st.markdown("---")
