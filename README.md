# python_chatbot
Simple Python chatbot using Ollama, capable of conversing via speech on general topics

## Initial Setup
To set up Ollama, follow the instructions in [their documentation](https://ollama.com/download). Specifically, you will need to install the `ollama` package and [pull the required LLaMA model](https://ollama.com/search).

## Ollama Package
This app uses the [ollama](https://pypi.org/project/ollama/) package to interact with the LLaMA model. The package is a Python wrapper around the LLaMA model, providing an easy-to-use interface for sending and receiving text messages. The model can be customized, but it requires the `llama3.2:1b` model to be installed and available on the system by default.

## Running the Code
To run the code, follow the steps below:

* Create a virtual environment: `python -m venv venv`
* Install the requirements: `pip install -r requirements.txt`
* Activate the virtual environment:
	+ On Windows: `venv\Scripts\activate`
	+ On Linux/Mac: `source venv/bin/activate`
* Run the code: `python main.py`
* This will start the chatbot and you can converse with it by speaking into your microphone. The chatbot will respond with text-to-speech responses.
* To exit the chatbot, say "exit chatbot".
