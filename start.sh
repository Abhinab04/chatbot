#!/bin/bash
pip install waitress
pip install SpeechRecognition pyttsx3 google-generativeai selenium requests beautifulsoup4 win10toast Flask
waitress-serve --port=$PORT flask_try:app
