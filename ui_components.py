import streamlit as st

def display_results(data: dict):
    """Renders the analysis results on the screen."""
    st.divider()
    st.subheader("Analysis Result")
    
    score = data["risk_score"]
    level = data["risk_level"]
    
    # Render Risk Badge
    if score >= 60:
        st.error(f"⚠️ {level} — Risk Score: {score}/100")
    elif score >= 30:
        st.warning(f"⚡ {level} — Risk Score: {score}/100")
    else:
        st.success(f"✅ {level} — Risk Score: {score}/100")

    st.write(f"**Assessment:** {data['advice_summary']}")

    # Render Red Flags
    if data.get("detected_flags"):
        st.markdown("**Identified Red Flags:**")
        for flag in data["detected_flags"]:
            st.markdown(f"- {flag}")
    
    # Render Reporting Buttons for High Risk
    if score >= 60:
        st.markdown("---")
        st.info("🚨 Protect others: Report this suspicious activity directly to the authorities.")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Report to CyberCrime.gov.in", "https://cybercrime.gov.in")
        with col2:
            st.link_button("SEBI SCORES Portal", "https://scores.sebi.gov.in")