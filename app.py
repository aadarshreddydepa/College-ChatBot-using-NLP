import streamlit as st
import json
import difflib

# Load the JSON data
with open("college_data.json", "r") as f:
    data = json.load(f)

# Streamlit Page Config
st.set_page_config(
    page_title="🎓 College Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Ghibli-style CSS with fixed input text color
ghibli_css = """
<style>
body {
    background-color: #fff8f0;
}
.chatbox {
    background-color: #fef6e4;
    border: 2px solid #fcd5ce;
    border-radius: 15px;
    padding: 20px;
    margin-top: 20px;
}
input[type="text"] {
    background-color: #fffaf0 !important;
    color: #3e2723 !important;
    border-radius: 8px;
    border: 1px solid #ffcad4;
    padding: 10px;
}
h1, h2, h3 {
    color: #7f5539;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
.response {
    background-color: #f0efeb;
    border-radius: 10px;
    padding: 10px;
    margin-top: 10px;
    border-left: 5px solid #d4a373;
    color: #4e342e;
    font-size: 16px;
}
</style>
"""

# Apply the custom CSS
st.markdown(ghibli_css, unsafe_allow_html=True)

# App title and intro
st.title("🏫 College Query Chatbot 🤖")
st.markdown("Ask me anything about our magical college ✨ (admissions, fees, placements, hostel, and more...)")

# User input field
user_input = st.text_input("💬 Your Question:")

# Simple matching logic
def get_response(user_input, data):
    for category, qa in data.items():
        questions = qa["questions"]
        match = difflib.get_close_matches(user_input.lower(), [q.lower() for q in questions], n=1, cutoff=0.4)
        if match:
            return qa["answer"]
    return "I'm not sure about that yet, but a magical owl might know. Try asking something else! 🦉"

# Show result
if user_input:
    response = get_response(user_input, data)
    st.markdown(f'<div class="response">🧚 {response}</div>', unsafe_allow_html=True)
