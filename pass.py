import streamlit as st
import re

# Page setup
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("😎 Is Your Password Hacker-Proof?")

# Intro
st.markdown("""
## 🔐 Welcome to Your Personal Password Strength Advisor!
##### Think your password is strong enough? Let's put it to the test!  
##### Get instant feedback and practical tips to build a **fortress of a password** 🛡️  
##### Stay safe, stay secure — one strong password at a time!
""")

# Input
password = st.text_input("🔑 Enter your password", type="password")

# Initialize score and feedback list
score = 0
feedback = []

# Password validation
if password:
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper and lower case check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should include at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")

    # Progress bar (score out of 4)
    st.markdown("## 📊 Password Strength Meter")
    st.progress(score / 4)

    # Final strength feedback
    if score == 4:
        st.success("✅ Your password is strong! 🥳")
    elif score == 3:
        st.warning("🟡 Your password is medium strength. Consider making it stronger.")
    else:
        st.error("🔴 Your password is weak. Please improve it.")

    # Suggestions if any
    if feedback:
        st.markdown("### 🛠️ Suggestions to Improve:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")
