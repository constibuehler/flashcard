import streamlit as st
import random

st.set_page_config(page_title="Flash Cards", page_icon="📚", layout="centered")

st.title("📚 Flash Card App")
st.write("Let's start learning languages the easy way!")

# --- Flashcard data ---
flashcards = [
    {"English": "hello", "German": "hallo", "French": "bonjour"},
    {"English": "goodbye", "German": "auf Wiedersehen", "French": "au revoir"},
    {"English": "please", "German": "bitte", "French": "s'il vous plaît"},
    {"English": "thank you", "German": "danke", "French": "merci"},
    {"English": "yes", "German": "ja", "French": "oui"},
    {"English": "no", "German": "nein", "French": "non"},
    {"English": "sorry", "German": "entschuldigung", "French": "désolé"},
]

# --- Language selection ---
languages = ["English", "German", "French"]
from_lang = st.selectbox("🔤 Language you know:", languages)
to_lang = st.selectbox("🌍 Language you want to learn:", languages, index=2)

if from_lang == to_lang:
    st.warning("Please choose two different languages.")
    st.stop()

# --- Flashcard logic ---
if "current_card" not in st.session_state:
    st.session_state.current_card = random.choice(flashcards)
    st.session_state.show_translation = False

def next_card():
    st.session_state.current_card = random.choice(flashcards)
    st.session_state.show_translation = False

def flip_card():
    st.session_state.show_translation = True

card = st.session_state.current_card

# --- Flashcard display ---
st.subheader(f"{from_lang}:")
st.markdown(f"### {card[from_lang]}")

if st.session_state.show_translation:
    st.subheader(f"{to_lang}:")
    st.markdown(f"### {card[to_lang]}")

# --- Buttons ---
col1, col2 = st.columns(2)
with col1:
    st.button("🔁 Flip", on_click=flip_card)
with col2:
    st.button("⏭️ Next", on_click=next_card)
