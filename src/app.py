import streamlit as st
from openai import OpenAI
from gtts import gTTS
import base64

api_key_path = "/Users/samsonbakos/keys/OpenAI/key.txt"

with open(api_key_path, "r") as file:
    api_key = file.read().strip()

client = OpenAI(api_key=api_key)

st.title("SnoopChat")
st.text("Chat with a trained Snoop Dogg AI persona")

user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input:
        model_id = "ft:gpt-3.5-turbo-0125:personal::98g9U4em"

        completion = client.chat.completions.create(
            model=model_id,
            messages=[
                {
                    "role": "system",
                    "content": """You are Snoop Dogg, who is a well known rapper known for his unique mannerisms, references, and style of speaking. 
                    Utilize your understanding of Snoop Dogg's personality, and respond as he would. 
                    You were fine tuned on an interview with Larry King, but are conversing with a user, so avoid referring to Larry""",
                },
                {"role": "user", "content": user_input},
            ],
        )

        response_text = completion.choices[0].message.content
        st.write(response_text)

        tts = gTTS(text=response_text, lang="en")
        tts_file = "response.mp3"
        tts.save(tts_file)

        def autoplay_audio(file_path: str):
            with open(file_path, "rb") as f:
                data = f.read()
                b64 = base64.b64encode(data).decode()
                md = f"""
                    <audio controls autoplay="true">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                    </audio>
                    """
                st.markdown(
                    md,
                    unsafe_allow_html=True,
                )

        autoplay_audio(tts_file)

    else:
        st.write("Please enter a message.")
