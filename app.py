import streamlit as st
import pandas as pd
import openai

# Set up OpenAI API
openai.api_key = "your_openai_api_key"

# Define function to generate response using OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      max_tokens=50
    )
    return response.choices[0].text.strip()

# Main function to run the chatbot
def main():
    st.title("Streamlit Chatbot")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load data from CSV
        data = pd.read_csv(uploaded_file)

        # Display chat interface
        user_input = st.text_input("You:", "")

        if st.button("Send"):
            if user_input:
                # Generate response using OpenAI API
                response = generate_response(user_input)

                # Display response
                st.text_area("Bot:", value=response, height=200)

if __name__ == "__main__":
    main()
