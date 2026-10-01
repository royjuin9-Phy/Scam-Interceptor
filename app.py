import streamlit as st
from PIL import Image
import pytesseract

from api_client import scan_message
from ui_components import display_results

st.set_page_config(page_title="FinShield Bharat", page_icon="🛡️", layout="centered")

st.title("🛡️ FinShield Bharat")
st.caption("Public Investor Protection Infrastructure — Verify Tips & Links Before Investing")

# Setup UI Tabs
tab1, tab2 = st.tabs(["Scan Text", "Scan Screenshot"])
user_text = ""

with tab1:
    user_text = st.text_area("Paste the WhatsApp / Telegram message here:", height=150)

with tab2:
    uploaded_file = st.file_uploader("Upload chat screenshot", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Screenshot", use_column_width=True)
        with st.spinner("Extracting text via OCR..."):
            try:
                extracted = pytesseract.image_to_string(image)
                user_text = extracted
                st.text_area("Extracted Text", value=user_text, height=100)
            except Exception:
                st.error("Tesseract OCR is not configured locally. Paste the text manually in Tab 1.")

# Main Action Button
if st.button("Analyze Risk", type="primary", use_container_width=True):
    if not user_text.strip():
        st.warning("Please provide a message or upload an image to analyze.")
    else:
        with st.spinner("Analyzing message safety..."):
            data, error_msg = scan_message(user_text)
            
            if error_msg:
                st.error(error_msg)
            else:
                display_results(data)