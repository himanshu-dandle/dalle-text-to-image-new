import openai
import requests
from PIL import Image
from io import BytesIO
import os
import re

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

def generate_image(prompt, resolution="512x512"):
    """
    Generate an image using OpenAI's DALL-E API and save it in the 'generated_images' folder.

    Args:
        prompt (str): The text prompt to generate the image.
        resolution (str): The desired image resolution ("256x256", "512x512", "1024x1024").

    Returns:
        str: The file name of the saved image.
    """
    try:
        # Request image generation
        print(f"\nGenerating an image for the prompt: '{prompt}' at resolution {resolution}...")
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Number of images to generate
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
        print(f"Image successfully saved as '{file_name}'\n")
        return file_name

    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None

def get_user_input():
    """
    Get the user's input for the prompt and resolution.

    Returns:
        tuple: A tuple containing the prompt (str) and resolution (str).
    """
    # Get the prompt from the user
    prompt = input("Enter your text prompt (e.g., 'A futuristic cityscape with flying cars'): ").strip()
    if not prompt:
        print("Prompt cannot be empty. Please try again.")
        return get_user_input()

    # Get the resolution from the user
    print("\nChoose image resolution:")
    print("1. 256x256")
    print("2. 512x512")
    print("3. 1024x1024")
    resolution_map = {"1": "256x256", "2": "512x512", "3": "1024x1024"}
    resolution_choice = input("Enter your choice (1/2/3): ").strip()
    resolution = resolution_map.get(resolution_choice, "512x512")  # Default to 512x512
    return prompt, resolution

def main():
    """
    Main function to run the interactive DALL-E image generator.
    """
    print("Welcome to the DALL-E Text-to-Image Generator!")
    print("Generate stunning images from your imagination.\n")
    
    while True:
        # Get user input
        prompt, resolution = get_user_input()
        
        # Generate the image
        file_name = generate_image(prompt, resolution)
        if file_name:
            print(f"Image ready: {file_name}")
        
        # Ask if the user wants to generate another image
        again = input("Would you like to generate another image? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the DALL-E Text-to-Image Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
