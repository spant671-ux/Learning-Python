# Problem 2: Text-to-Speech using the pyttsx3 library
import pyttsx3  # Import the text-to-speech library

engine = pyttsx3.init()  # Initialize the TTS engine
engine.say("I will speak this text")  # Queue the text to be spoken
engine.runAndWait()  # Process the speech queue and wait until done