import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model=genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[{"mime_type":uploaded_file.type,
                      "data":bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uplaoded")


st.set_page_config(page_title="Multilanguage Invoice Extractor App")
st.header("Google Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file=st.file_uploader("Choose an Image...",type=["jpg",'png','jpeg'])
iamge=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)

submit=st.button("Tell me about the Invoice")
input_prompt="""
You are an expert in understaing Invoices . User will uplozd an image , you has to answer the questions based on the invoice image given 
"""

if submit:
    image_data=input_image(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader(" the response is :")
    st.write(response)
