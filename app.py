import streamlit as st
import speech_recognition as sr
import os  # Import os module for file operations

# Initialize the recognizer
recognizer = sr.Recognizer()

# Streamlit app title and description
st.title("Speech Recognition Using AI")
st.write("This app converts speech to text from both real-time recording and uploaded audio files.")

# Option to choose between recording or uploading
option = st.selectbox("Select Input Method", ["Record from Microphone", "Upload Audio File"])

if option == "Record from Microphone":
    # Add a language code input box for recording
    language_code = st.text_input("Enter the language code (e.g., 'en-US' for English, 'hi-IN' for Hindi, 'te-IN' for Telugu):", "en-US")

    # Button to start recording
    if st.button("Start Recording"):
        with sr.Microphone() as source:
            st.write("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            st.write("Recording for up to 20 seconds...")

            try:
                # Listen to the microphone input
                recorded_audio = recognizer.listen(source, timeout=None, phrase_time_limit=20)
                st.write("Recording complete. Recognizing the text...")

                # Recognize the speech
                text = recognizer.recognize_google(recorded_audio, language=language_code)
                st.success("Decoded Text:")
                st.write(text)
            except sr.UnknownValueError:
                st.error("Google Speech Recognition could not understand the audio.")
            except sr.RequestError as e:
                st.error(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as ex:
                st.error(f"An error occurred: {ex}")

elif option == "Upload Audio File":
    # Add a language code input box for uploaded files
    language_code_upload = st.text_input("Enter the language code (e.g., 'en-US' for English, 'hi-IN' for Hindi, 'te-IN' for Telugu):", "en-US")

    # File uploader widget to upload audio file
    uploaded_file = st.file_uploader("Upload an audio file (WAV format)", type=["wav"])

    # Process the file if it is uploaded
    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with open("temp.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Load the audio file for recognition
        with sr.AudioFile("temp.wav") as source:
            st.write("Loading the audio file...")
            # Recognize the speech
            try:
                audio = recognizer.record(source)  # Read the entire audio file
                st.write("Recognizing the text...")
                text = recognizer.recognize_google(audio, language=language_code_upload)  # Use the uploaded language code
                st.success("Decoded Text:")
                st.write(text)
            except sr.UnknownValueError:
                st.error("Google Speech Recognition could not understand the audio.")
            except sr.RequestError as e:
                st.error(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as ex:
                st.error(f"An error occurred: {ex}")

# Cleanup temporary file if it exists
if os.path.exists("temp.wav"):
    try:
        os.remove("temp.wav")
    except Exception as e:
        st.warning(f"Could not remove temporary file: {e}")
