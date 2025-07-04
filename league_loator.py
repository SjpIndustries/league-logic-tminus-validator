import streamlit as st
from datetime import datetime, time, timedelta

st.set_page_config(page_title="LeagueLogic T-minus Validator", page_icon="🧠")

st.title("🧠 LeagueLogic T-minus Validator")
st.markdown("Check tactical compliance before executing your V4.3-TCR-EPI prompt.")

# Input: Separate Date and Time Inputs
kickoff_date = st.date_input("📅 Kickoff Date (AEST)", value=datetime(2025, 7, 5).date())
kickoff_time = st.time_input("⏰ Kickoff Time (AEST)", value=time(17, 30))

# Combine into full datetime object
kickoff_datetime = datetime.combine(kickoff_date, kickoff_time)

# Current AEST Time
now_aest = datetime.utcnow() + timedelta(hours=10)

# Calculate T-minus
t_minus = int((kickoff_datetime - now_aest).total_seconds() / 60)

# Tactical Status
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

# Display Output
st.markdown("---")
st.markdown(f"### 🕒 Current AEST Time: `{now_aest.strftime('%d/%m/%Y — %H:%M AEST')}`")
st.markdown(f"### 🎯 Kickoff Time: `{kickoff_datetime.strftime('%d/%m/%Y — %H:%M AEST')}`")
st.markdown(f"### ⏱️ T-minus: `{t_minus} minutes`")
st.markdown(f"### 🔒 Tactical Window Status: <span style='color:{color}; font-size: 1.4em;'>{status}</span>", unsafe_allow_html=True)

  
