from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai
from IPython.display import Markdown

# Load environment variables
load_dotenv()  # Take environment variables from .env

# Ensure API key is available
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API Key is missing. Please check your .env file.")
    st.stop()

# Configure the Gemini model API
genai.configure(api_key=api_key)

# Function to format responses to markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function to get a response from the Gemini model
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel('gemini-pro')  # Replace with the correct model if necessary
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Q&A Application")

# Create an input box for the question
input_text = st.text_input("Ask your question:", key="input")

submit = st.button("Submit")

# Handle the button click event
if submit:
    if input_text.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        response = get_gemini_response(input_text)
        st.subheader("Response:")
        st.write(response)
