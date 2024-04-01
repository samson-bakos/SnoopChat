import streamlit as st
from openai import OpenAI
from gtts import gTTS
from func import *
from charactr_api import CharactrAPISDK, Credentials

openai_api_key = st.secrets["OPENAI_API_KEY"]
charactr_api_key = st.secrets["CHARACTR_API_KEY"]
chacactr_client_key = st.secrets["CHARACTR_CLIENT_KEY"]

openai_client = OpenAI(api_key=openai_api_key)
sdk = CharactrAPISDK(
    Credentials(client_key=chacactr_client_key, api_key=charactr_api_key)
)

st.title("SnoopChat")
st.text("Chat with a Snoop Dogg AI persona")

voice = st.selectbox("Select a Voice:", ["Snoop Dogg", "Basic Text to Speech"])

user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input:
        model_id = "ft:gpt-3.5-turbo-0125:personal::98g9U4em"

        completion = openai_client.chat.completions.create(
            model=model_id,
            messages=[
                {
                    "role": "system",
                    "content": """You are Snoop Dogg, who is a well known rapper known for his unique mannerisms, references, and style of speaking. 
                    Utilize your understanding of Snoop Dogg's personality, and respond as he would. 
                    You were fine tuned on an interview with Larry King, but are conversing with a user, so never refer to Larry, or Mr.King. 
                    The person speaking with you is a just a regular user.""",
                },
                {"role": "user", "content": user_input},
            ],
        )

        response_text = completion.choices[0].message.content
        st.write(response_text)

        if voice == "Basic Text to Speech":
            tts = gTTS(text=response_text, lang="en")
            tts_file = "response.mp3"
            tts.save(tts_file)

            autoplay_audio(tts_file)

        if voice == "Snoop Dogg":
            # replace with correct id later
            snoop_voice_id = 143
            result = sdk.tts.convert(snoop_voice_id, response_text)
            if "data" in result:
                audio_content = result["data"]
                audio_file = "response_charactr.mp3"
                with open(audio_file, "wb") as f:
                    f.write(audio_content)
                autoplay_audio("response_charactr.mp3")
            else:
                st.error("Failed to retrieve audio data.")

    else:
        st.write("Please enter a message.")
