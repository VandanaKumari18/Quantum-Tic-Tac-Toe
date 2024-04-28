import math
import streamlit as st
from streamlit import cache
import streamlit.components.v1 as components

import numpy as np
import pandas as pd
from game import get_random_value, validate

def reset():
    del st.session_state['board']
    st.session_state.available_moves = list()

def perform_move(y, x):
    psi = '|ψ>'
    if st.session_state.board[x, y] == psi:
        user_value = get_random_value()
        st.session_state.board[x, y] = user_value
        user_flag = validate(st.session_state.board)

        if not user_flag:
            st.dataframe(st.session_state.board)
            reset()
            return 0

        comp_square = np.random.randint(1, 9)
        col = (comp_square - 1) % 3
        row = math.floor((comp_square - 1) / 3)
        comp_value = get_random_value()

        if st.session_state.board[row, col] == psi:
            st.session_state.board[row, col] = comp_value

        comp_flag = validate(st.session_state.board)

        if not comp_flag:
            st.dataframe(st.session_state.board)
            reset()
            return 0

        st.write("Computer move:", f"({col}, {row})")
        st.write("Computer value:", comp_value)
        st.write("User value:", user_value)
        st.dataframe(st.session_state.board)

    else:
        st.info("Already selected!")
        st.dataframe(st.session_state.board)

def main():
    menu = ["Play", "Instructions", "About"]
    option = st.sidebar.selectbox("Menu", menu)
    psi = '|ψ>'

    if option=="Play":
        st.subheader("Quantum play begins!")
        st.write("Default Computer --> |0>")
        st.write("Default User --> |1>")

        if 'board' not in st.session_state:
            st.session_state.board = np.array([[psi, psi, psi], [psi, psi, psi], [psi, psi, psi]])
            st.session_state.available_moves = ["Stand by", "(0, 0)", "(0, 1)", "(0, 2)", "(1, 0)", "(1, 1)", "(1, 2)", "(2, 0)", "(2, 1)", "(2, 2)"]

        move = st.selectbox("Make a move!", st.session_state.available_moves)
        if move == "Stand by":
            st.dataframe(st.session_state.board)
        elif move == "(0, 0)":
            perform_move(0, 0)
        elif move == "(0, 1)":
            perform_move(0, 1)
        elif move == "(0, 2)":
            perform_move(0, 2)
        elif move == "(1, 0)":
            perform_move(1, 0)
        elif move == "(1, 1)":
            perform_move(1, 1)
        elif move == "(1, 2)":
            perform_move(1, 2)
        elif move == "(2, 0)":
            perform_move(2, 0)
        elif move == "(2, 1)":
            perform_move(2, 1)
        elif move == "(2, 2)":
            perform_move(2, 2)

    elif option=="Instructions":
        st.subheader("Instructions")
        board = np.array([[psi,psi,psi], [psi,psi,psi], [psi,psi,psi]])
        st.write('Board:')
        st.dataframe(board)
        instruction_1 = """
        The above board represents the initial state of the game.
        |ф> represents the superposition state!
        Always, the user is given the chance to make the first move.
        [0> and |1> represent the piece chosen by the Computer and User respectively.
        However, unlike the classical tic tac toe, there's not a 100% probability that
        when computer/user make their move, it will result into their respective move.
        For eg, if user selects a piece, it's actually possible that the piece take the value of |0> and not |1>.
        This is the Quantum effect of Quantum Superposition in the Quantum Tic Tac Toe!
        """
        st.write(instruction_1)
    
    else:
        st.subheader('About')
        st.write('Group project - Quantum informatics')
        st.subheader('Author:')
        st.markdown("- Vandana Kumari")
        st.balloons()


if __name__ == '__main__':
    main()