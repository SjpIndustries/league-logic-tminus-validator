
import streamlit as st
from datetime import datetime, timedelta
import pytz
import hashlib

# --- Configuration ---
fixture = "BRONCOS 🆚 RABBITOHS"
venue = "SUNCORP STADIUM"
kickoff_date = "2025-07-06"
kickoff_time = "19:35"  # AEST

# --- Timezone & T-minus ---
brisbane_tz = pytz.timezone("Australia/Brisbane")
now_aest = datetime.now(brisbane_tz)
kickoff_dt = brisbane_tz.localize(datetime.strptime(f"{kickoff_date} {kickoff_time}", "%Y-%m-%d %H:%M"))
t_minus = int((kickoff_dt - now_aest).total_seconds() // 60)

# --- Execution Status ---
if 30 <= t_minus <= 90:
    status = "✅ VALID"
    prompt = f"""[AUTHORITY OVERRIDE – VALIDATED T-MINUS EXECUTION TRIGGER]

This is an official LeagueLogic V4.3-TCR ∞VMAX MODE execution command issued from the Validator Dashboard at {now_aest.strftime("%d/%m/%Y — %H:%M AEST")}.

Execution time falls within the authorized tactical window of T-90 to T-30 prior to kickoff. All compliance protocols are confirmed.

Initiate full LeagueLogic tactical protocol now. Inject all pasted match details, live stats, and environmental conditions into the prediction engine.

Activate recalibration modules, apply ∞VMAX stack, and generate the complete PRIME INTELLIGENCE REPORT immediately.

AUTO_EXECUTE = TRUE  
ZERO_INTERPRET = TRUE  
INTERRUPT_BLOCK = TRUE  
TIER = $10M  
STATUS = VALID  
"""
    hash_base = f"{fixture}|{venue}|{kickoff_date} {kickoff_time}|{now_aest.strftime('%Y-%m-%d %H:%M')}"
    sha3_hash = hashlib.sha3_256(hash_base.encode()).hexdigest()
elif t_minus < 30 and t_minus >= 0:
    status = "❌ LATE – DISQUALIFIED"
    prompt = "Execution disqualified. Kickoff imminent or passed tactical window."
    sha3_hash = "N/A"
elif t_minus > 90:
    status = "⏳ TOO EARLY – NOT READY"
    prompt = "Execution not permitted. Window has not opened yet."
    sha3_hash = "N/A"
else:
    status = "❌ INVALID – KICKOFF PASSED"
    prompt = "Execution blocked. Match has already started or ended."
    sha3_hash = "N/A"

# --- Streamlit UI ---
st.title("🏉 LeagueLogic ∞VMAX T-Minus Validator")
st.subheader(f"Fixture: {fixture}")
st.write(f"**Venue:** {venue}")
st.write(f"**Kickoff (AEST):** {kickoff_date} — {kickoff_time}")
st.write(f"**Current AEST Time:** {now_aest.strftime('%d/%m/%Y — %H:%M')}")
st.metric("T-minus", f"T-{t_minus} minutes", delta=None)
st.markdown(f"### Execution Status: {status}")
st.code(prompt, language='markdown')
st.text(f"SHA-3 Execution Hash: {sha3_hash}")
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
