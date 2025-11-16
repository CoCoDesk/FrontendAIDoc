import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Family AI Doctor",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# REMOVE STREAMLIT SIDEBAR + DEFAULT HEADER
# ---------------------------------------------------------
st.markdown("""
<style>
/* Hide default Streamlit elements */
[data-testid="stSidebar"],
[data-testid="stSidebarNav"],
header[data-testid="stHeader"],
#MainMenu,
footer {
    visibility: hidden !important;
}

/* Remove white padding */
.block-container, 
[data-testid="stAppViewBlockContainer"], 
[data-testid="stAppViewContainer"],
section.main > div {
    padding: 0 !important;
    margin: 0 !important;
}

/* Remove internal toolbar */
[data-testid="stToolbar"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Hide the sidebar */
[data-testid="stSidebar"] {
    display: none !important;
}

/* Force full width layout */
.main {
    margin-left: 0 !important;
    padding-left: 0 !important;
}

/* New Streamlit layout selectors */
[data-testid="stAppViewContainer"] {
    margin-left: 0 !important;
    padding-left: 0 !important;
}

[data-testid="stAppViewBlockContainer"] {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

/* Remove top blank space created by Streamlit header */
header[data-testid="stHeader"] {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none !important;
}
[data-testid="stSidebarNav"] {
    display: none !important;
}
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Remove Streamlit's internal padding */
.block-container {
    padding-left: 0 !important;
    padding-right: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
}

/* Removes phantom margin Streamlit adds */
[data-testid="stAppViewBlockContainer"] {
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
}

/* Removes leftover white space container */
[data-testid="stToolbar"] {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# GOOGLE FONTS + GLOBAL THEME
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body {
    font-family: 'Poppins', sans-serif !important;
    background: linear-gradient(135deg, #e8f3ff, #f0f7ff, #ffffff, #edf4ff);
    background-size: 400% 400%;
    animation: gradientMove 8s ease infinite;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Fix unwanted blank space */
[data-testid="stAppViewContainer"] {
    padding-top: 0 !important;
    margin-top: 0 !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Slightly darker medical patterned background */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #dbe4ff !important;  /* darker soft-blue */
    background-image: radial-gradient(#9bb3ff 1px, transparent 1px) !important;
    background-size: 18px 18px !important;
    background-attachment: fixed !important;
    background-repeat: repeat !important;
}

/* Keep the inner container transparent */
[data-testid="stAppViewBlockContainer"],
.block-container {
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ⭐ NAVBAR
# ---------------------------------------------------------
st.markdown("""
<style>
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background: linear-gradient(90deg, #001f4d, #003b88);
    padding: 20px 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 3px 15px rgba(0,0,0,0.26);
    z-index: 9999;
}
.navbar .logo {
    color: white;
    font-size: 28px;
    font-weight: 700;
}
.nav-links a {
    color: white;
    text-decoration: none;
    margin-left: 40px;
    font-size: 18px;
    font-weight: 500;
    transition: 0.3s;
}
.nav-links a:hover {
    color: #ffcc00;
    transform: translateY(-2px);
}
.body-gap {
    margin-top: 110px;
}
</style>

<div class="navbar">
    <div class="logo">🧠 Family AI Doctor</div>
    <div class="nav-links">
        <a href="/">Home</a>
        <a href="/?page=about">About</a>
        <a href="/?page=diseases">Diseases</a>
        <a href="/?page=contact">Contact Us</a>
    </div>
</div>

<div class="body-gap"></div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------
st.markdown("""
<style>
.hero {
    text-align: center;
    padding: 60px;
    background: linear-gradient(135deg, #003b88, #0058c9);
    color: white;
    border-radius: 20px;
    margin: 0px 40px 40px 40px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.25);
}
.hero h1 {
    font-size: 55px;
    font-weight: 700;
}
.hero p {
    font-size: 23px;
    color: #ffdd77;
}
</style>

<div class="hero">
    <h1>FAMILY AI DOCTOR</h1>
    <p>Your Smart Multi-Disease Screening Assistant</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# DISEASE CARDS
# ---------------------------------------------------------
st.markdown("""
<style>
/* Individual card styling */
.disease-card {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    color: white;
    text-align: center;
    padding: 35px 20px;
    border-radius: 20px;
    font-weight: 600;
    font-size: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    transition: transform 0.3s, box-shadow 0.3s;
}

/* Hover effect */
.disease-card:hover {
    transform: translateY(-8px) scale(1.05);
    box-shadow: 0 15px 35px rgba(0,0,0,0.35);
}

/* Emoji styling */
.disease-card span {
    font-size: 50px;
    display: block;
    margin-bottom: 15px;
}

/* Buttons styling */
.stButton button {
    background: #ffcc00 !important;
    color: #001f4d !important;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 600;
    cursor: pointer;
    transition: 0.3s;
}

.stButton button:hover {
    background: #ffd633 !important;
    transform: translateY(-2px);
}

/* Center buttons under cards */
.card-button {
    text-align: center;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

## ------------------- Row 1 -------------------
# ------------------- Row 1 -------------------
col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.markdown("<div class='disease-card'><span>🩸</span>Diabetes</div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='display:flex; justify-content:center; margin-top:10px;'>
    """, unsafe_allow_html=True)
    if st.button("Open Diabetes Page", key="db"):
        st.switch_page("pages/Diabetes.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='disease-card'><span>🧬</span>Cancer</div>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex; justify-content:center; margin-top:10px;'>", unsafe_allow_html=True)
    if st.button("Open Cancer Page", key="cancer"):
        st.switch_page("pages/Cancer.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='disease-card'><span>❤️</span>Heart Disease</div>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex; justify-content:center; margin-top:10px;'>", unsafe_allow_html=True)
    if st.button("Open Heart Disease Page", key="heart"):
        st.switch_page("pages/Heart_Disease.py")
    st.markdown("</div>", unsafe_allow_html=True)


# ------------------- Row 2 -------------------
col4, col5, col6 = st.columns(3, gap="large")
with col4:
    st.markdown("<div class='disease-card'><span>🩺</span>Kidney Disease</div>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex; justify-content:center; margin-top:10px;'>", unsafe_allow_html=True)
    if st.button("Open Kidney Disease Page", key="kidney"):
        st.switch_page("pages/Kidney_Disease.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col5:
    st.markdown("<div class='disease-card'><span>🫁</span>Liver Disease</div>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex; justify-content:center; margin-top:10px;'>", unsafe_allow_html=True)
    if st.button("Open Liver Disease Page", key="liver"):
        st.switch_page("pages/Liver_Disease.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col6:
    st.markdown("<div class='disease-card'><span>🧠</span>Parkinson's Disease</div>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex; justify-content:center; margin-top:10px;'>", unsafe_allow_html=True)
    if st.button("Open Parkinson's Page", key="parkinson"):
        st.switch_page("pages/Parkinsons.py")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------- PERFECT FLOATING CHATBOT BUTTON --------------------

# 1. CSS styles to target the Streamlit button
st.markdown("""
<style>
/* This container holds the visual elements (label + button) */
#chat-container {
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 99999;
    display: flex;
    flex-direction: column;
    align-items: center; /* Aligns circle to be centered */
}

/* Label box */
.chat-label {
    background: #003566;
    color: white;
    padding: 10px 18px;
    border-radius: 12px;
    font-size: 16px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
    font-weight: 500;
    margin-bottom: 8px;
}

/* This is the DIV that will WRAP the Streamlit button.
   We need it to apply our custom styles to the button inside.
*/
#chat-button-wrapper {
    width: 70px;
    height: 70px;
}

/* This targets the actual Streamlit button element INSIDE the wrapper */
#chat-button-wrapper button {
    width: 70px;         /* Make the button a circle */
    height: 70px;        /* Make the button a circle */
    padding: 0;          /* Remove default padding */
    border: none;        /* Remove default border */
    background: #003566; /* Set the background color */
    color: white;        /* Set the icon color */
    border-radius: 50%;  /* Make it a circle */
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    transition: 0.3s;
    font-size: 35px;     /* Size for the emoji */
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}

/* Hover effect for the button */
#chat-button-wrapper button:hover {
    transform: scale(1.12);
    background: #002244;
}
</style>
""", unsafe_allow_html=True)

# 2. The VISUAL and FUNCTIONAL button
# We place the label and the button wrapper inside the main container
st.markdown('<div id="chat-container">', unsafe_allow_html=True)

# Visual Label
st.markdown('<div class="chat-label">Instant Cure?<br>Talk to our AI DocBot</div>', unsafe_allow_html=True)

# Functional, Styled Button
# We place the button inside the wrapper div to style it
st.markdown('<div id="chat-button-wrapper">', unsafe_allow_html=True)
if st.button("🤖", key="floating_chat_button"): # Use emoji as button content
    st.switch_page("pages/AIDocBot.py")
st.markdown('</div>', unsafe_allow_html=True) # Close wrapper

st.markdown('</div>', unsafe_allow_html=True) # Close container


# ---------------------------------------------------------
# SUPER-SLIM FOOTER
# ---------------------------------------------------------
st.markdown("""
<style>
.footer {
    text-align: center;
    padding: 5px 0px;
    margin-top: 15px;
    font-size: 17px;
    color: white;
    background: linear-gradient(90deg, #001f4d, #003b88);
}
.footer-line {
    width: 100%;
    border: none;
    border-top: 1px solid #c9c9c9;
}
</style>

<div class="footer">
    <hr class="footer-line">
    © 2025 Family AI Doctor — All Rights Reserved
</div>
""", unsafe_allow_html=True)

