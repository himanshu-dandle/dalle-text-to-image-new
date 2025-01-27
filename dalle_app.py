import openai
import requests
from PIL import Image
from io import BytesIO
import os
import re
import streamlit as st

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

def generate_image(prompt, resolution="512x512"):
    """
    Generate an image using OpenAI's DALL-E API and return the file path.

    Args:
        prompt (str): The text prompt to generate the image.
        resolution (str): The desired image resolution ("256x256", "512x512", "1024x1024").

    Returns:
        str: The file path of the saved image.
    """
    try:
        # Request image generation
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=resolution
        )
        # Extract the image URL
        image_url = response['data'][0]['url']
        
        # Download the image
        img_response = requests.get(image_url)
        image = Image.open(BytesIO(img_response.content))
        
        # Ensure the 'generated_images' folder exists
        os.makedirs("generated_images", exist_ok=True)
        
        # Sanitize the file name
        safe_prompt = re.sub(r'[\\/*?:"<>|]', "", prompt)  # Remove invalid characters
        file_name = os.path.join("generated_images", f"{safe_prompt.replace(' ', '_')}_{resolution}.png")
        
        # Save the image locally
        image.save(file_name)
        return file_name

    except openai.error.OpenAIError as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit App
st.title("DALL-E Text-to-Image Generator")
st.markdown("### Generate stunning images from text prompts using OpenAI's DALL-E!")

# Input fields
prompt = st.text_input("Enter your prompt:", "A futuristic cityscape with flying cars")
resolution = st.radio("Select image resolution:", ["256x256", "512x512", "1024x1024"])

# Generate button
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating your image..."):
            file_name = generate_image(prompt, resolution)
            if file_name:
                st.image(file_name, caption=f"Generated Image ({resolution})", use_column_width=True)
                st.success(f"Image saved as: {file_name}")
    else:
        st.warning("Please enter a valid prompt!")
