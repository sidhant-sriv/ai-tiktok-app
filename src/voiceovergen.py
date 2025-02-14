from gtts import gTTS
import os


def generate_voiceover(
    text, output_file="file-server/static/audio/output_voiceover.mp3"
):
    """
    Generate a voiceover from text and save it as an audio file.

    Args:
        text (str): The text to convert to speech.
        output_file (str): The name of the output audio file (default: "output_voiceover.mp3").
    """
    # Initialize the TTS object
    tts = gTTS(text)

    # Save the speech as an audio file
    tts.save(output_file)

    # Play the generated audio (optional)
    return output_file
