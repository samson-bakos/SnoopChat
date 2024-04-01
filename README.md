# SnoopChat

Welcome to SnoopChat! This is a text-to-speech system that responds in the style and voice of Snoop Dogg. You can try it live at [SnoopChat](https://snoopchat.streamlit.app).

Please note, due to limited training data availability, SnoopChat is a work in progress. The Chatbot was fine tuned with actual transcripts of Snoop Dogg in order to capture a more authentic representation of his speech, rather than the highly exaggerated, stereotypical version given when simply asking a GPT model to speak like Snoop Dogg. However, because it was trained on only ~250 prompts from interviews, it may be overfit to this training data. Improvements could easily be made by rerunning the fine tuning scripts with a larger set of transcripts, if available. 

## Overview

SnoopChat combines natural language processing techniques with voice synthesis programs to create a virtual agent that embodies the personality and cadence of Snoop Dogg. The system operates through a web interface, allowing users to interact with Snoop Dogg's virtual counterpart by typing messages.

## Project Process

1. **Extracting Youtube Transcripts**: Initially, transcripts from SnoopDogTV's GGN segments were extracted. This data was processed using OpenAI's GPT-3.5 model to label speakers for each segment. However, the quality of this data proved to be lower than desired.

2. **Utilizing Long Interviews**: Recognizing the need for higher quality data, a long interview with Snoop Dogg conducted by Larry King was utilized. Using regex, the text was segmented into host prompts and Snoop's responses, resulting in improved data quality.

3. **Data Refinement**: The extracted interview data was reformatted and fed into GPT-3.5 for fine-tuning, allowing the model to better capture Snoop Dogg's conversational style and vocabulary.

4. **Audio Extraction and Transcription**: Audio clips from SnoopDoggTV interviews were extracted, specifically choosing segments where Snoop's voice was distinct from the speaker. Google Cloud Speech Recognition was employed to create labeled transcripts with speaker labels and timestamps.

5. **Voice Agent Training**: The segmented audio clips were used to train a gemelo.ai voice agent, capturing the nuances of Snoop Dogg's voice. This voice agent was then utilized for text-to-speech synthesis.

6. **Web Interface Development**: The SnoopChat system was hosted on Streamlit, providing a simple user interface for interacting with the virtual Snoop Dogg agent.

### Project Directory Structure

- **data/**: Contains raw data, excluding larger audio and video files.
- **model/**: Contains the model ID for the fine-tuned GPT.
- **training/**: Includes experimentation notebooks and Python scripts required for training.
- **src/**: Includes files necessary for the Streamlit app, including `requirements.txt`. Note that the requirements file is for running the app and not for the entire training process.

## Getting Started

To try SnoopChat, simply visit [SnoopChat](https://snoopchat.streamlit.app) and start typing your messages to interact with Snoop Dogg's virtual counterpart.

Thank you for using SnoopChat! If you have any questions or feedback, feel free to reach out to the project maintainer at samsonbakos@hotmail.com.
