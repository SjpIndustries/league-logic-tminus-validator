
import streamlit as st
from datetime import datetime, time, timedelta
import hashlib

st.set_page_config(page_title="LeagueLogic T-minus Validator", page_icon="🧠")

st.markdown(
    "<h1 style='color:#FFD700;'>🧠 LeagueLogic T-minus Validator</h1>",
    unsafe_allow_html=True
)
st.markdown("### <span style='color:white;'>Check tactical compliance before executing your <strong>V4.3-TCR-EPI</strong> prompt.</span>", unsafe_allow_html=True)

# Match Fixture Selector
fixtures = [
    "BULLDOGS vs. BRONCOS",
    "RAIDERS vs. DRAGONS",
    "COWBOYS vs. STORM",
    "ROOSTERS vs. TIGERS"
]
selected_fixture = st.selectbox("📋 Select Fixture", fixtures)

# Input: Separate Date and Time
kickoff_date = st.date_input("📅 Kickoff Date (AEST)", value=datetime(2025, 7, 5).date())
kickoff_time = st.time_input("⏰ Kickoff Time (AEST)", value=time(17, 30))

# Combine into full datetime object
kickoff_datetime = datetime.combine(kickoff_date, kickoff_time)

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

# Generate SHA-3 Hash
hash_input = f"{selected_fixture}_{now_aest.strftime('%H%M')}_AEST"
sha3_hash = hashlib.sha3_256(hash_input.encode()).hexdigest().upper()

# Output
st.markdown("---")
st.markdown(f"### 🕒 Current AEST Time: <span style='color:lightgreen;'>{now_aest.strftime('%d/%m/%Y — %H:%M AEST')}</span>", unsafe_allow_html=True)
st.markdown(f"### 🎯 Kickoff Time: <span style='color:deepskyblue;'>{kickoff_datetime.strftime('%d/%m/%Y — %H:%M AEST')}</span>", unsafe_allow_html=True)
st.markdown(f"### ⏱️ T-minus: <span style='color:violet;'>{t_minus} minutes</span>", unsafe_allow_html=True)
st.markdown(f"### 🔒 Tactical Window Status: <span style='color:{color}; font-size: 1.4em;'><strong>{status}</strong></span>", unsafe_allow_html=True)

# Show SHA-3 Hash
st.markdown("---")
st.markdown("### 🔐 Execution SHA-3 Hash:")
st.code(f"LLV4.3∞{selected_fixture.replace(' ', '')}{now_aest.strftime('%H%M')}AEST_SHA3 → {sha3_hash}", language="bash")

st.markdown("---")
st.markdown("<footer style='text-align: center; color: #888;'>∞VMAX Engine • LeagueLogic Tactical Validator</footer>", unsafe_allow_html=True)
