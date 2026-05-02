import streamlit as st
import random

st.set_page_config(page_title="Smart Guessing Game")

st.title("🎯 Smart Number Guessing Game")

# 🔹 Difficulty Selection
difficulty = st.selectbox(
    "Choose Difficulty",
    ["Easy (1–50, 10 attempts)", "Medium (1–100, 7 attempts)", "Hard (1–200, 5 attempts)"]
)

# 🔹 Set difficulty values
if difficulty == "Easy (1–50, 10 attempts)":
    low, high, max_attempts = 1, 50, 10
elif difficulty == "Medium (1–100, 7 attempts)":
    low, high, max_attempts = 1, 100, 7
else:
    low, high, max_attempts = 1, 200, 5

# 🔹 Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# 🔹 Input
guess = st.number_input(f"Enter your guess ({low}-{high}):", min_value=low, max_value=high)

# 🔹 Show attempts
st.write(f"Attempts: {st.session_state.attempts} / {max_attempts}")

# 🔹 Check button
if st.button("Check Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess == st.session_state.number:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True

    elif guess > st.session_state.number:
        st.warning("📉 Too High!")

    else:
        st.warning("📈 Too Low!")

    # 🔥 Hint system
    diff = abs(st.session_state.number - guess)
    if diff <= 5:
        st.info("🔥 Very Close!")
    elif diff <= 15:
        st.info("🙂 Close!")
    else:
        st.info("❄️ Far away!")

    # 🔹 Check attempts limit
    if st.session_state.attempts >= max_attempts and not st.session_state.game_over:
        st.error(f"💀 Game Over! The number was {st.session_state.number}")
        st.session_state.game_over = True

# 🔹 Restart button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.number = random.randint(low, high)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
