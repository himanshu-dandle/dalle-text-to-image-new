DALL-E Text-to-Image Generator
This project implements a DALL-E Text-to-Image Generator using OpenAI's API. It offers both a Command-Line Interface (CLI) and a Streamlit-based Web App for users to generate images from text prompts interactively.

Project Structure


project/
├── dalle_generate.py       # Command-line tool for image generation
├── dalle_app.py            # Streamlit-based web app
├── requirements.txt        # List of dependencies for the project
├── generated_images/       # Folder for storing generated images
│   ├── futuristic_city_512x512.png
│   ├── serene_beach_256x256.png
├── assets/                 # (Optional) Folder for README image examples
│   ├── example_image.png
│   ├── docker_build1.png
├── README.md               # Documentation for the project


Features
	CLI Tool:

		Accepts prompts and resolution inputs directly from the terminal.
		Saves generated images in a structured folder (generated_images/) with descriptive file names.
	Web App:

		User-friendly interface built with Streamlit.
		Allows users to input prompts, choose resolutions, and view generated images instantly.
	Image Output:

		Generated images are saved in a centralized folder (generated_images/).

Requirements
1. Python Version: Python 3.7 or higher
2. Dependencies:
		streamlit
		openai
		requests
		pillow
Install all dependencies using:
	pip install -r requirements.txt

Setup
1. Clone the Repository
	git clone https://github.com/himanshu-dandle/dalle-text-to-image.git
	cd dalle-text-to-image
2. Create a Virtual Environment
	python -m venv env
	source env/bin/activate  # On Windows: .\env\Scripts\activate

3. Install Dependencies
	pip install -r requirements.txt
4. Add OpenAI API Key
	Replace "YOUR_API_KEY" in dalle_generate.py and dalle_app.py with your OpenAI API key.


Usage
Command-Line Tool
1.Run the CLI script:
	python dalle_generate.py
2. Enter the required prompt and resolution when prompted.
3. The generated image will be saved in the generated_images/ folder.

Web App
1.Start the Streamlit app:
		streamlit run dalle_app.py
2. Open the link provided by Streamlit (e.g., http://localhost:8501).
3. Enter your prompt and select a resolution to generate an image.

Output
All generated images are saved in the generated_images/ folder with the naming convention:

	<prompt_text>_<resolution>.png
	Example
		For the prompt "A futuristic city with flying cars" at 512x512 resolution:

		Saved as: generated_images/futuristic_city_with_flying_cars_512x512.png
		
Sample Prompts
	Nature: "A serene beach with a pink sunset and palm trees"
	Futuristic: "A futuristic cityscape with flying cars under neon lights"
	Abstract: "An abstract painting of a dreamscape with floating islands"

Deployment
Deploy on Streamlit Cloud
	Push the project to a GitHub repository.
	Deploy on Streamlit Cloud:
		1) Log in with GitHub.
		2) Select your repository and specify dalle_app.py as the main file.
		3)Share the generated public URL.
		
Future Enhancements
	1)Add batch image generation for multiple prompts.
	2)Explore additional resolutions or advanced image styles.
	3)Integrate Stable Diffusion or other open-source image generation models.
	
License
This project is open-source under the MIT License.

