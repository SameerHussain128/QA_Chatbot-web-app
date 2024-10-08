import streamlit as st
import os
import google.generativeai as genai

# Set up your environment variable for Google Gemini API
os.environ['GEMINI_API_KEY'] = ''

# Configure the generative AI
genai.configure(api=os.environ['GEMINI_API_KEY'])

# Function to get AI response (can be adapted for different AI models)
def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Adjust model name
    response = model.generate_content([input_text])  # Generate content based on input text
    return response.text

# Streamlit app settings
st.set_page_config(page_title='AI Chatbot')

# Header for the chatbot
st.header("AI Chatbot Application")

# Input prompt from the user
user_input = st.text_input('You: ', key='input')

# Submit button
submit = st.button('Ask')

# When the user sends input, clear previous conversation
if submit and user_input:
    # Clear the session state (removes conversation history)
    st.session_state['conversation'] = []
    
    # Add user's input to conversation history
    st.session_state['conversation'].append(f"You: {user_input}")
    
    # Generate AI response
    bot_response = get_gemini_response(user_input)
    
    # Add bot's response to conversation history
    st.session_state['conversation'].append(f"Bot: {bot_response}")
    
    # Display the latest conversation
    for message in st.session_state['conversation']:
        st.write(message)