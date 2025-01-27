# DALL-E Text-to-Image Generator

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

This project is a web application that generates images based on text prompts using OpenAI's DALL-E API. Simply input a description, and the model will generate a unique image based on your prompt.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Example Generated Image](#example-generated-image)
3. [Features](#features)
   - [CLI Tool](#cli-tool)
   - [Web App](#web-app)
   - [Image Output](#image-output)
4. [Requirements](#requirements)
5. [Setup](#setup)
6. [Usage](#usage)
   - [Command-Line Tool](#command-line-tool)
   - [Web App](#web-app-1)
7. [Output](#output)
8. [Sample Prompts](#sample-prompts)
9. [Deployment](#deployment)
10. [Future Enhancements](#future-enhancements)
11. [License](#license)
12. [Acknowledgments](#acknowledgments)

## Project Structure
DALL-E_Text-to-Image/ │ ├── generated_images/ # Folder containing generated images │ ├── example_image1.png # Example generated image 1 │ └── example_image2.png # Example generated image 2 │ ├── .env # Environment variables file ├── dalle_app.py # Streamlit application script ├── dalle_generate.py # Script for local testing ├── requirements.txt # Python dependencies └── README.md # Project documentation


## Example Generated Image

![A panda eating bamboo under cherry blossoms](generated_images/A_panda_eating_bamboo_under_cherry_blossoms_1024x1024.png)

**Description**: A panda eating bamboo under cherry blossoms.

## Features

### CLI Tool:
- Accepts prompts and resolution inputs directly from the terminal.
- Saves generated images in a structured folder (`generated_images/`) with descriptive file names.

### Web App:
- User-friendly interface built with **Streamlit**.
- Allows users to input prompts, choose resolutions, and view generated images instantly.

### Image Output:
- Generated images are saved in a centralized folder (`generated_images/`) with meaningful names.

## Requirements

- **Python Version**: Python 3.7 or higher
- **Dependencies**:
  - streamlit
  - openai
  - requests
  - pillow

	Install all dependencies using:

	pip install -r requirements.txt

Setup
1. Clone the Repository:


	git clone https://github.com/himanshu-dandle/dalle-text-to-image.git
	cd dalle-text-to-image

2. Create a Virtual Environment:
	python -m venv env
	source env/bin/activate  # On Windows: .\env\Scripts\activate
3. Install Dependencies:
	pip install -r requirements.txt
4. Add OpenAI API Key:
	Replace YOUR_API_KEY in dalle_generate.py and dalle_app.py with your OpenAI API key.

Usage
Command-Line Tool
1.Run the CLI script:


	python dalle_generate.py
	Enter the required prompt and resolution when prompted.
	The generated image will be saved in the generated_images/ folder.
	
Web App

1. Start the Streamlit app:


	streamlit run dalle_app.py
2. Open the link provided by Streamlit (e.g., http://localhost:8501).
3. Enter your prompt and select a resolution to generate an image.
4. The generated image will be displayed on the web app.

Output
All generated images are saved in the generated_images/ folder with the naming convention:
	<prompt_text>_<resolution>.png
Example:

For the prompt "A futuristic city with flying cars" at 512x512 resolution:
**Saved as: generated_images/futuristic_city_with_flying_cars_512x512.png

## Sample Prompts

- **Nature**: "A serene beach with a pink sunset and palm trees"
- **Futuristic**: "A futuristic cityscape with flying cars under neon lights"
- **Abstract**: "An abstract painting of a dreamscape with floating islands"



## Deployment

### Deploy on Streamlit Cloud
1. Push the project to a GitHub repository.
2. Deploy on **Streamlit Cloud**:
   1. Log in to Streamlit Cloud using your **GitHub** account.
   2. Select your repository and specify `dalle_app.py` as the main file.
   3. After deployment, Streamlit will provide a public URL for your app.
   4. Share this URL to access the deployed app.


## Future Enhancements

- Add batch image generation for multiple prompts.
- Explore additional resolutions or advanced image styles.
- Integrate **Stable Diffusion** or other open-source image generation models.


## License

This project is open-source under the **MIT License**. You can freely use, modify, and distribute the code as long as you include the license.

Acknowledgments
***OpenAI for the DALL-E API
***Streamlit for the web application framework
***Inspired by similar projects in the community