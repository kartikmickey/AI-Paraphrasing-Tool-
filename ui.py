import streamlit as st
from pydantic import BaseModel
from typing import List
from helpers import structured_generator  # Assuming this is a predefined function in the helpers module

# Define the BaseModel class for data validation
class Titles(BaseModel):
    titles: List[str]

# Streamlit code to create the UI
def main():
    # Set up the title and description of the web app
    st.title("Text Paraphrasing Tool")
    st.write("Paraphrase the given text using AI")

    # Input section: User inputs the topic for the blog titles
    user_input = st.text_input("Enter the text to paraphrase", "A paraphrase is a restatement of the meaning of a text or passage using other words. ")

    # Button to trigger the title generation
    if st.button("Paraphrase Text"):
        # Call the structured_generator function with the user input
        prompt = f"paraphrase the following text: {user_input}"
        openai_model = "gpt-3.5-turbo"
        result = structured_generator(openai_model, prompt, Titles)

        # Display the generated titles
        if result.titles:
            st.subheader("Generated Titles")
            for title in result.titles:
                st.write(title)
        else:
            st.write("No titles were generated. Try a different topic.")

# Protect the script to run only when it's the main module
if __name__ == "__main__":
    main()