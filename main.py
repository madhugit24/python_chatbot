import speech_recognition as sr
import ollama
import pyttsx3

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the Ollama client
client = ollama.Client()

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def listen_to_voice_command():
    """
    Listen to voice commands from the microphone and return the text transcription
    """
    with sr.Microphone() as source:
        print("Please say something:")
        audio = r.listen(source)
        try:
            # Use Google's speech recognition API to transcribe the audio
            text = r.recognize_google(audio)
            print("You said: " + text)
            if text.lower() == "exit app":
                print("Exiting the chatbot. Goodbye!")
                exit()
            else:
                return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand your audio")
            return None
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(
                    e
                )
            )
            return None


def get_llama_response(prompt):
    """
    Send the prompt to the LLaMA model and return the response
    """
    model = "llama3.2:1b"
    response = client.generate(model=model, prompt=prompt)
    return response.response


def speak_text(text):
    """
    Use the text-to-speech engine to speak the text
    """
    engine.say(text)
    engine.runAndWait()


def main():
    """
    Main loop for the chatbot

    This function will continuously listen to voice commands, get the response from the LLaMA model, and speak the response
    """
    while True:
        # Listen to voice commands
        text = listen_to_voice_command()
        if text is not None:
            # Get the LLaMA response
            response = get_llama_response(text)
            print("Response from LLaMA:")
            print(response)
            # Speak the response
            speak_text(response)


if __name__ == "__main__":
    main()
