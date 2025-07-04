import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="LeagueLogic T-minus Validator", page_icon="🧠")

st.title("🧠 LeagueLogic T-minus Validator")
st.markdown("Check tactical compliance before executing your V4.3-TCR-EPI prompt.")

# Input: Kickoff Date and Time
kickoff_datetime = st.datetime_input("📅 Kickoff Time (AEST)", value=datetime(2025, 7, 5, 17, 30))

# Current AEST Time
now_aest = datetime.utcnow() + timedelta(hours=10)

# Calculate T-minus in minutes
t_minus = int((kickoff_datetime - now_aest).total_seconds() / 60)

# Determine status
if 30 <= t_minus <= 90:
    status = "✅ VALID: Supreme Accuracy"
    color = "green"
elif 0 < t_minus < 30:
    status = "⚠️ WARNING: Accuracy May Be Reduced"
    color = "orange"
elif t_minus <= 0:
    status = "❌ DISQUALIFIED EXECUTION"
    color = "red"
else:
    status = "⚠️ TOO EARLY: Not within tactical window"
    color = "gray"

# Output
st.markdown("---")
st.markdown(f"### 🕒 Current AEST Time: `{now_aest.strftime('%d/%m/%Y — %H:%M AEST')}`")
st.markdown(f"### 🎯 Kickoff Time: `{kickoff_datetime.strftime('%d/%m/%Y — %H:%M AEST')}`")
st.markdown(f"### ⏱️ T-minus: `{t_minus} minutes`")
st.markdown(f"### 🔒 Tactical Window Status: <span style='color:{color}; font-size: 1.4em;'>{status}</span>", unsafe_allow_html=True)
