import streamlit as st

st.set_page_config(page_title="Phishing Awareness Training", page_icon="🛡️")

st.title("🛡️ Phishing Awareness Training Module")

st.header("What is Phishing?")
st.write("""
Phishing is a cyber attack where attackers impersonate trusted organizations
to steal sensitive information such as usernames, passwords, banking details,
or personal information.
""")

st.header("Common Types of Phishing")
st.markdown("""
- Email Phishing
- Spear Phishing
- Smishing (SMS Phishing)
- Vishing (Voice Phishing)
- Clone Phishing
""")

st.header("How to Identify Phishing Emails")
st.markdown("""
✅ Check the sender's email address carefully.

✅ Watch for urgent language like:
- "Your account will be suspended"
- "Immediate action required"

✅ Avoid clicking suspicious links.

✅ Look for spelling and grammar mistakes.

✅ Verify unexpected attachments before opening them.
""")

st.header("How to Identify Fake Websites")
st.markdown("""
🔍 Check the URL carefully.

🔍 Look for HTTPS.

🔍 Beware of lookalike domains.

🔍 Check website design quality and trust indicators.
""")

st.header("Social Engineering Tactics")
st.markdown("""
Attackers often use:

- Fear
- Urgency
- Curiosity
- Authority
- Rewards or prizes

to trick users into revealing information.
""")

st.header("Best Practices")
st.markdown("""
✔ Use strong passwords

✔ Enable Multi-Factor Authentication (MFA)

✔ Keep software updated

✔ Never share passwords

✔ Verify requests through official channels

✔ Report suspicious emails immediately
""")

st.header("Real-World Example")

st.warning("""
Example:

Email Subject: Your Bank Account Has Been Locked

Message:
Dear Customer,

Your account has been locked. Click the link below immediately to verify your identity.

https://secure-bank-login-verify.com

This is likely a phishing attempt because:
- Creates urgency
- Suspicious URL
- Requests sensitive information
""")

st.header("Interactive Quiz")

score = 0

q1 = st.radio(
    "1. Which is a common sign of a phishing email?",
    [
        "Official company newsletter",
        "Urgent request for personal information",
        "Normal account notification"
    ]
)

if q1 == "Urgent request for personal information":
    score += 1

q2 = st.radio(
    "2. What should you do before clicking a link?",
    [
        "Click immediately",
        "Check the URL carefully",
        "Forward it to friends"
    ]
)

if q2 == "Check the URL carefully":
    score += 1

q3 = st.radio(
    "3. What is MFA?",
    [
        "Multiple File Access",
        "Multi-Factor Authentication",
        "Mail Forwarding Application"
    ]
)

if q3 == "Multi-Factor Authentication":
    score += 1

if st.button("Submit Quiz"):
    st.success(f"Your Score: {score}/3")

    if score == 3:
        st.balloons()
        st.success("Excellent! You understand phishing awareness.")
    elif score == 2:
        st.info("Good job! Review a few concepts.")
    else:
        st.warning("Please review the training material and try again.")

st.header("Conclusion")
st.write("""
Phishing attacks are one of the most common cyber threats.
Awareness, careful verification, and good security practices
can greatly reduce the risk of becoming a victim.
""")