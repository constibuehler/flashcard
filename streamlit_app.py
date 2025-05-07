# streamlit_app.py
import streamlit as st
import random
from flashcards_data import flashcards

# --- App Setup ---
st.set_page_config(page_title="My Flash Cards", page_icon="📚", layout="centered")

# --- Initialize State ---
def init_state():
    st.session_state.done = []
    st.session_state.still_learning = []
    st.session_state.current_card = random.choice(flashcards)
    st.session_state.feedback = ""
    st.session_state.correct = False
    st.session_state.show_hint = False
    st.session_state.user_input = ""
    st.session_state.attempts = 0
    st.session_state.learn_only = False

# --- Select Next Card ---
def next_card():
    source = st.session_state.still_learning if st.session_state.learn_only and st.session_state.still_learning else flashcards
    st.session_state.current_card = random.choice(source)
    st.session_state.feedback = ""
    st.session_state.correct = False
    st.session_state.show_hint = False
    st.session_state.user_input = ""
    st.session_state.attempts = 0
    st.rerun()

# --- Check Answer ---
def check_answer(user_input, correct_answer):
    return user_input.strip().lower() == correct_answer.strip().lower()

# --- App Logic ---
def main():
    st.title("📚 My Flash Cards")
    st.write("Translate the word and train your brain!")

    languages = ["English", "German", "French", "Portuguese", "Italian"]

    from_lang = st.selectbox("🔤 Language you know:", languages)
    to_lang = st.selectbox("🌍 Language you want to learn:", languages, index=2)

    if from_lang == to_lang:
        st.warning("Please choose two different languages.")
        st.stop()

    if "current_card" not in st.session_state:
        init_state()

    card = st.session_state.current_card
    st.subheader(f"Translate from {from_lang} to {to_lang}:")
    st.markdown(f"### {card[from_lang]}")

    st.session_state.user_input = st.text_input("Your translation:", value=st.session_state.user_input)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✅ Check"):
            correct_answer = card[to_lang]
            if check_answer(st.session_state.user_input, correct_answer):
                st.session_state.feedback = "✅ Correct!"
                st.session_state.correct = True
                if card not in st.session_state.done:
                    st.session_state.done.append(card)
                next_card()
            else:
                st.session_state.attempts += 1
                st.session_state.feedback = f"❌ Wrong ({st.session_state.attempts}/3). Try again or ask for a hint."
                if card not in st.session_state.still_learning:
                    st.session_state.still_learning.append(card)
                if st.session_state.attempts >= 3:
                    st.warning(f"The correct answer was: **{correct_answer}**")
                    next_card()

    with col2:
        if st.button("💡 Hint"):
            st.session_state.show_hint = True

    with col3:
        if st.button("⏭️ Skip"):
            if card not in st.session_state.still_learning:
                st.session_state.still_learning.append(card)
            next_card()

    if st.session_state.feedback:
        st.markdown(f"**{st.session_state.feedback}**")

    if st.session_state.show_hint:
        st.info(f"Hint: starts with **{card[to_lang][:2]}...**")

    st.checkbox("🎯 Practice only 'Still Learning' words", key="learn_only")

    # --- Progress ---
    with st.expander("📊 Progress"):
        st.write(f"✅ Done: {len(st.session_state.done)} cards")
        st.write(f"🧠 Still Learning: {len(st.session_state.still_learning)} cards")
        if st.checkbox("Show 'Done' cards"):
            for c in st.session_state.done:
                st.write(f"{c[from_lang]} → {c[to_lang]}")
        if st.checkbox("Show 'Still Learning' cards"):
            for c in st.session_state.still_learning:
                st.write(f"{c[from_lang]} → {c[to_lang]}")

if __name__ == "__main__":
    main()
    