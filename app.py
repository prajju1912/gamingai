import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="⚔️ AI Arena: Crypto Combat", page_icon="🧠", layout="centered")
st.image("https://img.icons8.com/color/96/joystick.png", width=100)
st.markdown("<h1 style='text-align: center; color: red;'>⚔️ AI Arena: Crypto Combat</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🤖 Battle against AI. Claim your victory. Save your name on the blockchain.</h3>", unsafe_allow_html=True)
st.markdown("---")

username = st.text_input("👤 Enter your warrior name:")

if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.ai_score = 0
    st.session_state.round = 1
    st.session_state.battle_log = []

moves = ['⚔️ Attack', '🛡️ Defend', '💥 Power-Up']

if username:
    st.subheader(f"🎮 Round {st.session_state.round}")
    player_move = st.radio("👉 Choose your move:", moves)
    if st.button("🔥 Submit Move"):
        ai_move = random.choice(moves)
        result = ""
        if player_move == ai_move:
            result = "⚖️ It's a draw!"
        elif (player_move == '⚔️ Attack' and ai_move == '💥 Power-Up') or              (player_move == '🛡️ Defend' and ai_move == '⚔️ Attack') or              (player_move == '💥 Power-Up' and ai_move == '🛡️ Defend'):
            st.session_state.player_score += 1
            result = "✅ You win this round!"
        else:
            st.session_state.ai_score += 1
            result = "❌ AI wins this round!"

        st.session_state.round += 1
        st.session_state.battle_log.append(
            f"🧍 {username} → {player_move} | 🤖 AI → {ai_move} → **{result}**"
        )

    st.markdown("### 📜 Battle Log:")
    for log in st.session_state.battle_log:
        st.success(log)

    st.markdown(f"#### 🧍 {username}'s Score: `{st.session_state.player_score}`")
    st.markdown(f"#### 🤖 AI's Score: `{st.session_state.ai_score}`")

    if st.session_state.round > 3:
        st.markdown("---")
        st.success("🏁 Battle Completed!")
        if st.session_state.player_score > st.session_state.ai_score:
            st.balloons()
            st.markdown(f"🎉 **{username} WINS the match!** 🎉")
            st.markdown("📝 **Blockchain Save Instruction**")
            st.code(f'saveResult("{username}", {st.session_state.player_score})  // Remix Call', language='solidity')
            st.markdown("💾 Copy the above command and paste it in Remix to store your result permanently.")
        elif st.session_state.player_score < st.session_state.ai_score:
            st.markdown("🤖 **AI WINS! Try again to beat it!**")
        else:
            st.markdown("⚔️ It's a tie! Rematch?")

        if st.button("🔄 Restart Game"):
            for key in ['player_score', 'ai_score', 'round', 'battle_log']:
                st.session_state[key] = 0 if 'score' in key else []
