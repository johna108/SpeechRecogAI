# Speech Recognition AI

A powerful and user-friendly speech recognition application built with Python and Streamlit that converts speech to text in multiple languages. The application supports both real-time recording and audio file uploads.

## Features

- **Real-time Speech Recognition**: Record audio directly through your microphone
- **Audio File Upload**: Process pre-recorded WAV audio files
- **Multi-language Support**: Supports various languages through language codes (e.g., 'en-US' for English, 'hi-IN' for Hindi, 'te-IN' for Telugu)
- **User-friendly Interface**: Built with Streamlit for a clean and intuitive user experience
- **Ambient Noise Adjustment**: Automatically adjusts for background noise during recording
- **Error Handling**: Robust error handling for various scenarios

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SpeechRecogAI.git
cd SpeechRecogAI
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Required Dependencies

- streamlit
- SpeechRecognition
- pyaudio (for microphone input)

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Choose your input method:
   - **Record from Microphone**: Speak directly into your microphone
   - **Upload Audio File**: Upload a pre-recorded WAV file

3. Enter the language code for your speech (e.g., 'en-US' for English)

4. Follow the on-screen instructions to either:
   - Start recording (20-second limit)
   - Upload an audio file

5. View the transcribed text output

## Supported Languages

The application supports multiple languages through Google Speech Recognition. Some common language codes include:

- English (US): 'en-US'
- Hindi: 'hi-IN'
- Telugu: 'te-IN'
- Spanish: 'es-ES'
- French: 'fr-FR'
- German: 'de-DE'

## Project Structure

```
SpeechRecogAI/
  ├── app.py              # Main application file
  ├── requirements.txt    # Project dependencies
  ├── README.md          # Project documentation
  └── sample_audio/      # Sample audio files for testing
      ├── long_audio.mp3
      └── speech.wav
```

## Error Handling

The application includes robust error handling for:
- Unrecognizable speech
- Google Speech Recognition service issues
- File handling errors
- General exceptions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Speech recognition powered by [Google Speech Recognition](https://cloud.google.com/speech-to-text) 