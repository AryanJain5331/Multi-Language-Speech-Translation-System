import speech_recognition as sr

def recognize_speech():
    """Recognizes speech from the microphone."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n🎤 Speak something... (Listening)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("✅ Recognized Text:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio. Try again.")
        return None
    except sr.RequestError:
        print("❌ Could not request results. Check your internet connection.")
        return None
