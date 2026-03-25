import streamlit as st
import numpy as np
import random
import time

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Tic-Tac-Toe", page_icon="🎮", layout="centered")

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Press+Start+2P&display=swap');

/* --- Global --- */
html, body, [class*="css"] {
    font-family: 'Orbitron', monospace !important;
    background-color: #0a0a0f !important;
    color: #e0e0f0 !important;
}

.stApp {
    background: #0a0a0f;
    background-image:
        linear-gradient(rgba(0,245,255,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,245,255,0.025) 1px, transparent 1px);
    background-size: 40px 40px;
}

/* --- Title --- */
.game-title {
    font-family: 'Press Start 2P', monospace !important;
    font-size: 22px;
    letter-spacing: 4px;
    color: #00f5ff;
    text-shadow: 0 0 20px #00f5ff99, 0 0 60px #00f5ff44;
    text-align: center;
    padding: 16px 0 8px 0;
    animation: flicker 4s infinite;
}

@keyframes flicker {
    0%,95%,100% { opacity: 1; }
    96%  { opacity: 0.7; }
    97%  { opacity: 1; }
    98%  { opacity: 0.5; }
}

/* --- Score board --- */
.score-row {
    display: flex;
    justify-content: center;
    gap: 20px;
    align-items: center;
    margin: 12px 0;
}

.score-box {
    background: #12121a;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    padding: 12px 28px;
    text-align: center;
    min-width: 110px;
    transition: all 0.3s;
}

.score-box.active-x { border-color: #00f5ff; box-shadow: 0 0 16px #00f5ff33; }
.score-box.active-o { border-color: #ff2d78; box-shadow: 0 0 16px #ff2d7833; }

.score-label  { font-size: 9px; letter-spacing: 2px; color: #555570; margin-bottom: 4px; }
.score-label.x { color: #00f5ff; }
.score-label.o { color: #ff2d78; }
.score-num    { font-size: 32px; font-weight: 900; }
.score-num.x  { color: #00f5ff; text-shadow: 0 0 20px #00f5ff88; }
.score-num.o  { color: #ff2d78; text-shadow: 0 0 20px #ff2d7888; }
.vs-text      { font-size: 18px; font-weight: 900; color: #555570; }

/* --- Status --- */
.status-bar {
    text-align: center;
    font-size: 11px;
    letter-spacing: 3px;
    margin: 6px 0 14px 0;
    min-height: 22px;
    padding: 6px 0;
}
.status-bar.x-turn  { color: #00f5ff; }
.status-bar.o-turn  { color: #ff2d78; }
.status-bar.result  { color: #e0e0f0; font-size: 14px; font-weight: 700; }
.status-bar.draw    { color: #aaaacc; font-size: 13px; }

/* --- Board --- */
.board-wrap {
    display: flex;
    justify-content: center;
    margin: 0 auto 20px auto;
}

/* Hide Streamlit button default styles; restyle as cells */
div[data-testid="column"] .stButton > button {
    width: 140px !important;
    height: 140px !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 52px !important;
    font-weight: 900 !important;
    background: #0a0a0f !important;
    border: 1.5px solid #1e1e2e !important;
    border-radius: 10px !important;
    color: #e0e0f0 !important;
    transition: all 0.15s !important;
    padding: 0 !important;
    line-height: 1 !important;
    cursor: pointer !important;
}

div[data-testid="column"] .stButton > button:hover {
    background: #16161f !important;
    border-color: #333350 !important;
    transform: scale(1.05) !important;
}

/* X cells */
.x-cell button {
    color: #00f5ff !important;
    font-weight: 900 !important;
    font-size: 58px !important;
    text-shadow: 0 0 20px #00f5ff88, 0 0 40px #00f5ff44 !important;
    border-color: #00f5ff55 !important;
    background: #001f22 !important;
    cursor: default !important;
}

/* O cells */
.o-cell button {
    color: #ff2d78 !important;
    font-weight: 900 !important;
    font-size: 58px !important;
    text-shadow: 0 0 20px #ff2d7888, 0 0 40px #ff2d7844 !important;
    border-color: #ff2d7855 !important;
    background: #220010 !important;
    cursor: default !important;
}

/* Win highlight */
.win-x button {
    color: #00f5ff !important;
    border-color: #00f5ff !important;
    background: #002a2e !important;
    box-shadow: inset 0 0 20px #00f5ff33, 0 0 24px #00f5ff55 !important;
    animation: winPop 0.5s ease !important;
}
.win-o button {
    color: #ff2d78 !important;
    border-color: #ff2d78 !important;
    background: #2e0015 !important;
    box-shadow: inset 0 0 20px #ff2d7833, 0 0 24px #ff2d7855 !important;
    animation: winPop 0.5s ease !important;
}

@keyframes winPop {
    0%   { transform: scale(1); }
    40%  { transform: scale(1.15); }
    70%  { transform: scale(0.95); }
    100% { transform: scale(1.06); }
}

/* --- Buttons row --- */
.stButton > button {
    font-family: 'Orbitron', monospace !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* New Game btn */
.new-game-btn .stButton > button {
    background: transparent !important;
    border: 1.5px solid #00f5ff !important;
    color: #00f5ff !important;
    border-radius: 8px !important;
    padding: 10px 22px !important;
    height: auto !important;
    width: auto !important;
    font-size: 10px !important;
}
.new-game-btn .stButton > button:hover {
    background: #00f5ff !important;
    color: #0a0a0f !important;
    box-shadow: 0 0 20px #00f5ff88 !important;
}

/* Reset Scores btn */
.reset-btn .stButton > button {
    background: transparent !important;
    border: 1.5px solid #555570 !important;
    color: #555570 !important;
    border-radius: 8px !important;
    padding: 10px 22px !important;
    height: auto !important;
    width: auto !important;
    font-size: 10px !important;
}
.reset-btn .stButton > button:hover {
    border-color: #e0e0f0 !important;
    color: #e0e0f0 !important;
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; max-width: 520px !important; }

/* Remove extra spacing around columns */
div[data-testid="column"] { padding: 3px !important; }
</style>
""", unsafe_allow_html=True)


# ── Game logic ─────────────────────────────────────────────────────────────────
def check_win(board, player):
    b = board
    lines = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for line in lines:
        if all(b[i] == player for i in line):
            return line
    return None

def is_full(board):
    return all(v != 0 for v in board)

def computer_move(board):
    empty = [i for i, v in enumerate(board) if v == 0]
    return random.choice(empty) if empty else None


# ── Session state init ─────────────────────────────────────────────────────────
def init_state():
    if "board" not in st.session_state:
        st.session_state.board     = [0] * 9
        st.session_state.game_over = False
        st.session_state.status    = ("YOUR TURN", "x-turn")
        st.session_state.win_cells = []
        st.session_state.score_x   = 0
        st.session_state.score_o   = 0
        st.session_state.turn      = 1   # 1=human, -1=cpu

init_state()

s = st.session_state


# ── Title ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="game-title">TIC · TAC · TOE</div>', unsafe_allow_html=True)


# ── Scoreboard ─────────────────────────────────────────────────────────────────
ax = "active-x" if s.turn == 1  and not s.game_over else ""
ao = "active-o" if s.turn == -1 and not s.game_over else ""

st.markdown(f"""
<div class="score-row">
  <div class="score-box {ax}">
    <div class="score-label x">YOU · X</div>
    <div class="score-num x">{s.score_x}</div>
  </div>
  <div class="vs-text">VS</div>
  <div class="score-box {ao}">
    <div class="score-label o">CPU · O</div>
    <div class="score-num o">{s.score_o}</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Status bar ─────────────────────────────────────────────────────────────────
msg, cls = s.status
st.markdown(f'<div class="status-bar {cls}">{msg}</div>', unsafe_allow_html=True)


# ── Board ──────────────────────────────────────────────────────────────────────
SYMBOLS = {0: " ", 1: "X", -1: "O"}

def cell_class(idx):
    v = s.board[idx]
    if idx in s.win_cells:
        return "win-x" if v == 1 else "win-o"
    if v == 1:  return "x-cell"
    if v == -1: return "o-cell"
    return ""

for row in range(3):
    cols = st.columns(3, gap="small")
    for col_idx in range(3):
        idx = row * 3 + col_idx
        css_cls = cell_class(idx)
        label   = SYMBOLS[s.board[idx]]

        with cols[col_idx]:
            st.markdown(f'<div class="{css_cls}">', unsafe_allow_html=True)
            clicked = st.button(label, key=f"cell_{idx}", disabled=(s.board[idx] != 0 or s.game_over))
            st.markdown('</div>', unsafe_allow_html=True)

            if clicked and not s.game_over and s.board[idx] == 0:
                # Human move
                s.board[idx] = 1
                win = check_win(s.board, 1)
                if win:
                    s.win_cells = win
                    s.score_x  += 1
                    s.status    = ("🎉  YOU WIN!", "result")
                    s.game_over = True
                elif is_full(s.board):
                    s.status    = ("IT'S A DRAW!", "draw")
                    s.game_over = True
                else:
                    # Computer move
                    s.status = ("THINKING...", "o-turn")
                    move = computer_move(s.board)
                    if move is not None:
                        s.board[move] = -1
                        cpu_win = check_win(s.board, -1)
                        if cpu_win:
                            s.win_cells = cpu_win
                            s.score_o  += 1
                            s.status    = ("COMPUTER WINS!", "result")
                            s.game_over = True
                        elif is_full(s.board):
                            s.status    = ("IT'S A DRAW!", "draw")
                            s.game_over = True
                        else:
                            s.turn   = 1
                            s.status = ("YOUR TURN", "x-turn")

                st.rerun()


# ── Buttons ────────────────────────────────────────────────────────────────────
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
_, c1, c2, _ = st.columns([1, 2, 2, 1])

with c1:
    st.markdown('<div class="new-game-btn">', unsafe_allow_html=True)
    if st.button("NEW GAME", key="new_game"):
        s.board     = [0] * 9
        s.game_over = False
        s.win_cells = []
        s.turn      = 1
        s.status    = ("YOUR TURN", "x-turn")
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
    if st.button("RESET SCORES", key="reset_scores"):
        s.board     = [0] * 9
        s.game_over = False
        s.win_cells = []
        s.turn      = 1
        s.status    = ("YOUR TURN", "x-turn")
        s.score_x   = 0
        s.score_o   = 0
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)