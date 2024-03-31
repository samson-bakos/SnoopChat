import base64
import streamlit as st
import requests
import json


def autoplay_audio(file_path: str):
    """Autoplay audio if not browser restricted"""
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


def get_api_key(path):
    with open(path, "r") as file:
        return file.read().strip()
