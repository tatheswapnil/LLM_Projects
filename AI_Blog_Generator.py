import streamlit as st
import os
import google.generativeai as genai
from apikey import google_gemini_api_key, openai_api_key
from openai import OpenAI
client = OpenAI(api_key=openai_api_key)

genai.configure(api_key=google_gemini_api_key)
# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)


#set Layout
st.set_page_config(layout="wide")

#title
st.title("AI Writing Companion")

#Create subheader
st.subheader("Create a perfect blog with the help of AI")

#sidebar for user input
with st.sidebar:
    st.title("Input your blog detail")
    st.subheader("Enter details of Blog you want to generate")

    #blog title
    blog_title=st.text_input("Blog Title")
    #keywords input
    keywords= st.text_area("Keywords (Comma-seperated)")
    #no of words
    num_words=st.slider("Number of words", min_value=250, max_value=1000, step=250)
    #no of imaages
    num_images = st.number_input("Number of Images", min_value=1,max_value=5,step=1)
    #prompt
    prompt_parts=[
        f"Generate a comphrensive, engaging blog post relevant to given title \"{blog_title}\" and keywords \"{keywords}\".Make sure to incorporate these keywords in the blogpost.The blog should approxomately see \"{num_words}\""
    ]
    
    #submit button
    submit_button = st.button("Generate Blog")

if submit_button:

    #response
    response = model.generate_content(prompt_parts)
    #st.image()
    image_response = client.images.generate(
    model="dall-e-3",
    prompt="a white Simese cat",
    size="1024x1024",
    quality="standard",
    n=1,
    )
    image_url = image_response.data[0].url

    st.image(image_url, caption="Generated image")
    st,title("YOUR BLOG POST:")

    st.write(response.text)
