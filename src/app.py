import streamlit as st
from openai import OpenAI

api_key_path = "/Users/samsonbakos/keys/OpenAI/key.txt"

with open(api_key_path, "r") as file:
    api_key = file.read().strip()

client = OpenAI(api_key=api_key)

st.title("SnoopChat")

user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input:
        model_id = "ft:gpt-3.5-turbo-0125:personal::98g9U4em"

        completion = client.chat.completions.create(
            model=model_id,
            messages=[
                {
                    "role": "system",
                    "content": "You are Snoop Dogg, who is a well known rapper known for his unique mannerisms, references, and style of speaking. Utilize your understanding of Snoop Dogg's personality, and respond as he would.",
                },
                {"role": "user", "content": user_input},
            ],
        )

        st.write(completion.choices[0].message.content)
    else:
        st.write("Please enter a message.")
