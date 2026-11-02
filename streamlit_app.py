import streamlit as st
import urllib.parse
import google.generativeai as genai

st.set_page_config(page_title="Fibu AI", page_icon="⚡", layout="centered")

st.markdown("""
<h1 style='text-align:center'>⚡ Fibu AI</h1>
<p style='text-align:center'>Text & Image Generator - Made by You</p>
<hr>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("Fibu AI Settings")
api_key = st.sidebar.text_input("Paste Gemini API Key (free from aistudio.google.com)", type="password")
st.sidebar.markdown("[Get FREE Key Here](https://aistudio.google.com/app/apikey)")

if api_key:
    genai.configure(api_key=api_key)

tab1, tab2 = st.tabs(["📝 Fibu Writer", "🎨 Fibu Vision"])

with tab1:
    st.subheader("Ask Fibu Anything")
    prompt = st.text_area("Your prompt:", "Write a cool app description for Fibu AI", height=120)
    if st.button("Generate Text ⚡", use_container_width=True):
        if not api_key:
            st.error("Please add your free Gemini API Key in sidebar first!")
        else:
            with st.spinner("Fibu is thinking..."):
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                st.success("Done!")
                st.write(response.text)

with tab2:
    st.subheader("Draw with Fibu")
    img_prompt = st.text_area("Describe your image:", "A cute robot mascot for Fibu AI, blue and purple, futuristic", height=120)
    style = st.selectbox("Style", ["Realistic", "Anime", "3D Render", "Cartoon", "Cyberpunk"])
    
    if st.button("Generate Image 🎨", use_container_width=True):
        full_prompt = f"{img_prompt}, {style} style, high quality, detailed"
        encoded = urllib.parse.quote(full_prompt)
        # Using Pollinations - 100% free, no key needed
        image_url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=102
