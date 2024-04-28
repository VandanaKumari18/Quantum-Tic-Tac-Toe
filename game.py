from qiskit import QuantumCircuit
from qiskit_aer import Aer
import numpy as np
import streamlit as st

def quantum_superposition():
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)
    
    simulator = Aer.get_backend('aer_simulator')
    result = simulator.run(circuit).result().get_counts()
    return result

def get_random_value():
    res = quantum_superposition()
    values = list(res.values())
    keys = list(res.keys())
    random_value = '|' + str(keys[np.argmax(values)]) + '>'
    return random_value

def validate(arr):

    flag = True
    zero_ket = '|0>'
    one_ket = '|1>'

    # Checks for the principal diagonal condition w.r.t. user
    if arr[0, 0] == one_ket and arr[1, 1] == one_ket and arr[2, 2] == one_ket:
        st.success("User has won!", icon="✅")
        st.balloons()
        flag = False

    # Checks for the principal diagonal confition w.r.t computer
    elif arr[0, 0] == zero_ket and arr[1, 1] == zero_ket and arr[2, 2] == zero_ket:
        st.error("Computer has won!", icon="🚨")
        st.snow()
        flag = False

    # Checks for the second diagonal condition w.r.t. user
    if arr[0, 2] == one_ket and arr[1, 1] == one_ket and arr[2, 0] == one_ket:
        st.success("User has won!", icon="✅")
        st.balloons()
        flag = False

    # Checks for the second diagonal confition w.r.t computer
    elif arr[0, 2] == zero_ket and arr[1, 1] == zero_ket and arr[2, 0] == zero_ket:
        st.error("Computer has won!", icon="🚨")
        st.snow()
        flag = False

    if flag:
        # Checks if any of the row conquered by user
        for index in [0, 1, 2]:
            if (list(arr[index]) == [one_ket, one_ket, one_ket]):
                st.success("User has won!", icon="✅")
                st.balloons()
                return 0

        # Checks if any of the row conquered by computer
        for index in [0, 1, 2]:
            if (list(arr[index]) == [zero_ket, zero_ket, zero_ket]):
                st.error("Computer has won!", icon="🚨")
                st.snow()
                return 0

        # Checks if any of the row conquered by user
        for index in [0, 1, 2]:
            if (list(arr[:, index]) == [one_ket, one_ket, one_ket]):
                st.success("User has won!", icon="✅")
                st.balloons()
                return 0

        # Checks if any of the row conquered by computer
        for index in [0, 1, 2]:
            if (list(arr[:, index]) == [zero_ket, zero_ket, zero_ket]):
                st.error("Computer has won!", icon="🚨")
                st.snow()
                return 0

        # Checks if it's not a draw
        if '|ψ>' not in arr:
            st.info("It's a draw!", icon="ℹ️")
            return 0

        return 1
    else:
        return 0