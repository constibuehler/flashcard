import streamlit as st
import random

# --- Page setup ---
st.set_page_config(page_title="My Flash Cards", page_icon="📚", layout="centered")
st.title("📚 My Flash Cards")
st.write("Translate the word and train your brain!")

# --- Flashcard data ---
flashcards = [
    {"English": "hello", "German": "hallo", "French": "bonjour", "Italian": "ciao", "Portuguese": "olá"},
    {"English": "goodbye", "German": "auf Wiedersehen", "French": "au revoir", "Italian": "arrivederci", "Portuguese": "adeus"},
    {"English": "please", "German": "bitte", "French": "s'il vous plaît", "Italian": "per favore", "Portuguese": "por favor"},
    {"English": "thank you", "German": "danke", "French": "merci", "Italian": "grazie", "Portuguese": "obrigado/obrigada"},
    {"English": "sorry", "German": "entschuldigung", "French": "désolé(e)", "Italian": "mi dispiace", "Portuguese": "desculpe"},
    {"English": "yes", "German": "ja", "French": "oui", "Italian": "sì", "Portuguese": "sim"},
    {"English": "no", "German": "nein", "French": "non", "Italian": "no", "Portuguese": "não"},
    {"English": "man", "German": "Mann", "French": "homme", "Italian": "uomo", "Portuguese": "homem"},
    {"English": "woman", "German": "Frau", "French": "femme", "Italian": "donna", "Portuguese": "mulher"},
    {"English": "child", "German": "Kind", "French": "enfant", "Italian": "bambino/bambina", "Portuguese": "criança"},
    {"English": "boy", "German": "Junge", "French": "garçon", "Italian": "ragazzo", "Portuguese": "menino"},
    {"English": "girl", "German": "Mädchen", "French": "fille", "Italian": "ragazza", "Portuguese": "menina"},
    {"English": "father", "German": "Vater", "French": "père", "Italian": "padre", "Portuguese": "pai"},
    {"English": "mother", "German": "Mutter", "French": "mère", "Italian": "madre", "Portuguese": "mãe"},
    {"English": "brother", "German": "Bruder", "French": "frère", "Italian": "fratello", "Portuguese": "irmão"},
    {"English": "sister", "German": "Schwester", "French": "sœur", "Italian": "sorella", "Portuguese": "irmã"},
    {"English": "friend", "German": "Freund", "French": "ami/amie", "Italian": "amico/amica", "Portuguese": "amigo/amiga"},
    {"English": "house", "German": "Haus", "French": "maison", "Italian": "casa", "Portuguese": "casa"},
    {"English": "home", "German": "Zuhause", "French": "domicile", "Italian": "casa", "Portuguese": "lar"},
    {"English": "car", "German": "Auto", "French": "voiture", "Italian": "macchina", "Portuguese": "carro"},
    {"English": "bus", "German": "Bus", "French": "autobus", "Italian": "autobus", "Portuguese": "ônibus"},
    {"English": "train", "German": "Zug", "French": "train", "Italian": "treno", "Portuguese": "trem"},
    {"English": "plane", "German": "Flugzeug", "French": "avion", "Italian": "aereo", "Portuguese": "avião"},
    {"English": "bicycle", "German": "Fahrrad", "French": "bicyclette", "Italian": "bicicletta", "Portuguese": "bicicleta"},
    {"English": "road", "German": "Straße", "French": "route", "Italian": "strada", "Portuguese": "estrada"},
    {"English": "street", "German": "Straße", "French": "rue", "Italian": "via", "Portuguese": "rua"},
    {"English": "school", "German": "Schule", "French": "école", "Italian": "scuola", "Portuguese": "escola"},
    {"English": "teacher", "German": "Lehrer", "French": "professeur", "Italian": "insegnante", "Portuguese": "professor/professora"},
    {"English": "student", "German": "Schüler", "French": "étudiant(e)", "Italian": "studente/studentessa", "Portuguese": "estudante"},
    {"English": "book", "German": "Buch", "French": "livre", "Italian": "libro", "Portuguese": "livro"},
    {"English": "pen", "German": "Stift", "French": "stylo", "Italian": "penna", "Portuguese": "caneta"},
    {"English": "paper", "German": "Papier", "French": "papier", "Italian": "carta", "Portuguese": "papel"},
    {"English": "computer", "German": "Computer", "French": "ordinateur", "Italian": "computer", "Portuguese": "computador"},
    {"English": "phone", "German": "Telefon", "French": "téléphone", "Italian": "telefono", "Portuguese": "telefone"},
    {"English": "table", "German": "Tisch", "French": "table", "Italian": "tavolo", "Portuguese": "mesa"},
    {"English": "chair", "German": "Stuhl", "French": "chaise", "Italian": "sedia", "Portuguese": "cadeira"},
    {"English": "bed", "German": "Bett", "French": "lit", "Italian": "letto", "Portuguese": "cama"},
    {"English": "door", "German": "Tür", "French": "porte", "Italian": "porta", "Portuguese": "porta"},
    {"English": "window", "German": "Fenster", "French": "fenêtre", "Italian": "finestra", "Portuguese": "janela"},
    {"English": "kitchen", "German": "Küche", "French": "cuisine", "Italian": "cucina", "Portuguese": "cozinha"},
    {"English": "bathroom", "German": "Badezimmer", "French": "salle de bains", "Italian": "bagno", "Portuguese": "banheiro"},
    {"English": "food", "German": "Essen", "French": "nourriture", "Italian": "cibo", "Portuguese": "comida"},
    {"English": "water", "German": "Wasser", "French": "eau", "Italian": "acqua", "Portuguese": "água"},
    {"English": "bread", "German": "Brot", "French": "pain", "Italian": "pane", "Portuguese": "pão"},
    {"English": "milk", "German": "Milch", "French": "lait", "Italian": "latte", "Portuguese": "leite"},
    {"English": "coffee", "German": "Kaffee", "French": "café", "Italian": "caffè", "Portuguese": "café"},
    {"English": "tea", "German": "Tee", "French": "thé", "Italian": "tè", "Portuguese": "chá"},
    {"English": "fruit", "German": "Obst", "French": "fruit", "Italian": "frutta", "Portuguese": "fruta"},
    {"English": "vegetable", "German": "Gemüse", "French": "légume", "Italian": "verdura", "Portuguese": "legume"},
    {"English": "meat", "German": "Fleisch", "French": "viande", "Italian": "carne", "Portuguese": "carne"},
    {"English": "fish", "German": "Fisch", "French": "poisson", "Italian": "pesce", "Portuguese": "peixe"},
    {"English": "egg", "German": "Ei", "French": "œuf", "Italian": "uovo", "Portuguese": "ovo"},
    {"English": "salt", "German": "Salz", "French": "sel", "Italian": "sale", "Portuguese": "sal"},
    {"English": "sugar", "German": "Zucker", "French": "sucre", "Italian": "zucchero", "Portuguese": "açúcar"},
    {"English": "day", "German": "Tag", "French": "jour", "Italian": "giorno", "Portuguese": "dia"},
    {"English": "night", "German": "Nacht", "French": "nuit", "Italian": "notte", "Portuguese": "noite"},
    {"English": "morning", "German": "Morgen", "French": "matin", "Italian": "mattina", "Portuguese": "manhã"},
    {"English": "evening", "German": "Abend", "French": "soir", "Italian": "sera", "Portuguese": "noite"},
    {"English": "week", "German": "Woche", "French": "semaine", "Italian": "settimana", "Portuguese": "semana"},
    {"English": "month", "German": "Monat", "French": "mois", "Italian": "mese", "Portuguese": "mês"},
    {"English": "year", "German": "Jahr", "French": "an", "Italian": "anno", "Portuguese": "ano"},
    {"English": "today", "German": "heute", "French": "aujourd'hui", "Italian": "oggi", "Portuguese": "hoje"},
    {"English": "tomorrow", "German": "morgen", "French": "demain", "Italian": "domani", "Portuguese": "amanhã"},
    {"English": "yesterday", "German": "gestern", "French": "hier", "Italian": "ieri", "Portuguese": "ontem"},
    {"English": "time", "German": "Zeit", "French": "temps", "Italian": "tempo", "Portuguese": "tempo"},
    {"English": "hour", "German": "Stunde", "French": "heure", "Italian": "ora", "Portuguese": "hora"},
    {"English": "minute", "German": "Minute", "French": "minute", "Italian": "minuto", "Portuguese": "minuto"},
    {"English": "second", "German": "Sekunde", "French": "seconde", "Italian": "secondo", "Portuguese": "segundo"},
    {"English": "weather", "German": "Wetter", "French": "temps", "Italian": "tempo", "Portuguese": "tempo"},
    {"English": "sun", "German": "Sonne", "French": "soleil", "Italian": "sole", "Portuguese": "sol"},
    {"English": "rain", "German": "Regen", "French": "pluie", "Italian": "pioggia", "Portuguese": "chuva"},
    {"English": "snow", "German": "Schnee", "French": "neige", "Italian": "neve", "Portuguese": "neve"},
    {"English": "wind", "German": "Wind", "French": "vent", "Italian": "vento", "Portuguese": "vento"},
    {"English": "cloud", "German": "Wolke", "French": "nuage", "Italian": "nuvola", "Portuguese": "nuvem"},
    {"English": "hot", "German": "heiß", "French": "chaud", "Italian": "caldo", "Portuguese": "quente"},
    {"English": "cold", "German": "kalt", "French": "froid", "Italian": "freddo", "Portuguese": "frio"},
    {"English": "warm", "German": "warm", "French": "tiède", "Italian": "tiepido", "Portuguese": "morno"},
    {"English": "cool", "German": "kühl", "French": "frais", "Italian": "fresco", "Portuguese": "fresco"},
    {"English": "happy", "German": "glücklich", "French": "heureux/heureuse", "Italian": "felice", "Portuguese": "feliz"},
    {"English": "sad", "German": "traurig", "French": "triste", "Italian": "triste", "Portuguese": "triste"},
    {"English": "angry", "German": "wütend", "French": "en colère", "Italian": "arrabbiato/arrabbiata", "Portuguese": "zangado/zangada"},
    {"English": "tired", "German": "müde", "French": "fatigué/fatiguée", "Italian": "stanco/stanca", "Portuguese": "cansado/cansada"},
    {"English": "sick", "German": "krank", "French": "malade", "Italian": "malato/malata", "Portuguese": "doente"},
    {"English": "strong", "German": "stark", "French": "fort/forte", "Italian": "forte", "Portuguese": "forte"},
    {"English": "weak", "German": "schwach", "French": "faible", "Italian": "debole", "Portuguese": "fraco/fraca"},
    {"English": "big", "German": "groß", "French": "grand/grande", "Italian": "grande", "Portuguese": "grande"},
    {"English": "small", "German": "klein", "French": "petit/petite", "Italian": "piccolo/piccola", "Portuguese": "pequeno/pequena"},
    {"English": "long", "German": "lang", "French": "long", "Italian": "lungo", "Portuguese": "longo"},
    {"English": "short", "German": "kurz", "French": "court", "Italian": "breve", "Portuguese": "curto"},
    {"English": "fast", "German": "schnell", "French": "rapide", "Italian": "veloce", "Portuguese": "rápido"},
    {"English": "slow", "German": "langsam", "French": "lent", "Italian": "lento", "Portuguese": "devagar"},
    {"English": "new", "German": "neu", "French": "nouveau/nouvelle", "Italian": "nuovo/nuova", "Portuguese": "novo/nova"},
    {"English": "old", "German": "alt", "French": "vieux/vieille", "Italian": "vecchio/vecchia", "Portuguese": "velho/velha"},
    {"English": "young", "German": "jung", "French": "jeune", "Italian": "giovane", "Portuguese": "jovem"},
    {"English": "beautiful", "German": "schön", "French": "beau/belle", "Italian": "bello/bella", "Portuguese": "bonito/bonita"},
    {"English": "ugly", "German": "hässlich", "French": "laid/laide", "Italian": "brutto/brutta", "Portuguese": "feio/feia"},
    {"English": "clean", "German": "sauber", "French": "propre", "Italian": "pulito/pulita", "Portuguese": "limpo/limpa"},
    {"English": "dirty", "German": "schmutzig", "French": "sale", "Italian": "sporco/sporca", "Portuguese": "sujo/suja"},
    {"English": "easy", "German": "einfach", "French": "facile", "Italian": "facile", "Portuguese": "fácil"},
    {"English": "difficult", "German": "schwierig", "French": "difficile", "Italian": "difficile", "Portuguese": "difícil"},
    {"English": "good", "German": "gut", "French": "bon/bonne", "Italian": "buono/buona", "Portuguese": "bom/boa"},
    {"English": "bad", "German": "schlecht", "French": "mauvais/mauvaise", "Italian": "cattivo/cattiva", "Portuguese": "mau/má"},
    {"English": "right", "German": "richtig", "French": "correct/correcte", "Italian": "giusto", "Portuguese": "certo"},
    {"English": "wrong", "German": "falsch", "French": "faux/fausse", "Italian": "sbagliato", "Portuguese": "errado"},
    {"English": "open", "German": "offen", "French": "ouvert", "Italian": "aperto", "Portuguese": "aberto"},
    {"English": "closed", "German": "geschlossen", "French": "fermé", "Italian": "chiuso", "Portuguese": "fechado"},
    {"English": "high", "German": "hoch", "French": "haut", "Italian": "alto", "Portuguese": "alto"},
    {"English": "low", "German": "niedrig", "French": "bas", "Italian": "basso", "Portuguese": "baixo"},
    {"English": "near", "German": "nah", "French": "près", "Italian": "vicino", "Portuguese": "perto"},
    {"English": "far", "German": "fern", "French": "loin", "Italian": "lontano", "Portuguese": "longe"},
    {"English": "here", "German": "hier", "French": "ici", "Italian": "qui", "Portuguese": "aqui"},
    {"English": "there", "German": "dort", "French": "là", "Italian": "là", "Portuguese": "lá"},
    {"English": "up", "German": "oben", "French": "en haut", "Italian": "su", "Portuguese": "cima"},
    {"English": "down", "German": "unten", "French": "en bas", "Italian": "giù", "Portuguese": "baixo"},
    {"English": "in", "German": "in", "French": "dans", "Italian": "in", "Portuguese": "em"},
    {"English": "out", "German": "aus", "French": "dehors", "Italian": "fuori", "Portuguese": "fora"},
    {"English": "on", "German": "auf", "French": "sur", "Italian": "su", "Portuguese": "sobre"},
    {"English": "off", "German": "aus", "French": "éteint", "Italian": "spento", "Portuguese": "desligado"},
    {"English": "under", "German": "unter", "French": "sous", "Italian": "sotto", "Portuguese": "debaixo"},
    {"English": "over", "German": "über", "French": "au-dessus", "Italian": "sopra", "Portuguese": "sobre"},
    {"English": "before", "German": "vor", "French": "avant", "Italian": "prima", "Portuguese": "antes"},
    {"English": "after", "German": "nach", "French": "après", "Italian": "dopo", "Portuguese": "depois"},
    {"English": "first", "German": "erste", "French": "premier/première", "Italian": "primo/prima", "Portuguese": "primeiro/primeira"},
    {"English": "last", "German": "letzte", "French": "dernier/dernière", "Italian": "ultimo/ultima", "Portuguese": "último/última"}
]

languages = ["English", "German", "French"]

# --- Session State Initialization ---
if "done" not in st.session_state:
    st.session_state.done = []
if "still_learning" not in st.session_state:
    st.session_state.still_learning = []
if "current_card" not in st.session_state:
    st.session_state.current_card = random.choice(flashcards)
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "correct" not in st.session_state:
    st.session_state.correct = False
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# --- Language selection ---
from_lang = st.selectbox("🔤 Language you know:", languages)
to_lang = st.selectbox("🌍 Language you want to learn:", languages, index=2)

if from_lang == to_lang:
    st.warning("Please choose two different languages.")
    st.stop()

card = st.session_state.current_card

st.subheader(f"Translate this word from {from_lang} to {to_lang}:")
st.markdown(f"### {card[from_lang]}")

# --- User Input ---
st.session_state.user_input = st.text_input("Your translation:", value=st.session_state.user_input)

# --- Check Answer ---
if st.button("Check"):
    correct_answer = card[to_lang].lower().strip()
    user_answer = st.session_state.user_input.lower().strip()

    if user_answer == correct_answer:
        st.session_state.feedback = "✅ Correct! Well done!"
        st.session_state.correct = True
        if card not in st.session_state.done:
            st.session_state.done.append(card)
    else:
        st.session_state.feedback = "❌ Not quite. Try again or ask for a hint!"
        st.session_state.correct = False
        if card not in st.session_state.still_learning:
            st.session_state.still_learning.append(card)

# --- Show feedback ---
if st.session_state.feedback:
    st.markdown(f"**{st.session_state.feedback}**")

# --- Hint logic ---
if not st.session_state.correct and st.session_state.feedback:
    if st.button("💡 Show Hint"):
        st.session_state.show_hint = True

if st.session_state.show_hint and not st.session_state.correct:
    hint = card[to_lang][:2] + "..."
    st.info(f"Hint: starts with **{hint}**")

# --- Next card ---
if st.session_state.correct:
    if st.button("⏭️ Next"):
        st.session_state.current_card = random.choice(flashcards)
        st.session_state.feedback = ""
        st.session_state.correct = False
        st.session_state.show_hint = False
        st.session_state.user_input = ""
        st.rerun()  # resets view immediately

# --- Progress tracking ---
with st.expander("📊 Progress"):
    st.write(f"✅ Done: {len(st.session_state.done)} cards")
    st.write(f"🧠 Still Learning: {len(st.session_state.still_learning)} cards")
    if st.checkbox("Show 'Done' cards"):
        for c in st.session_state.done:
            st.write(f"{c[from_lang]} → {c[to_lang]}")
    if st.checkbox("Show 'Still Learning' cards"):
        for c in st.session_state.still_learning:
            st.write(f"{c[from_lang]} → {c[to_lang]}")

