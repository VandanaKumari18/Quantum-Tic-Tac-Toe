<h1 align="center">Quantum Tic-Tac-Toe</h1>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#installation">Installation</a> •
  <a href="#screenshots">Screenshots</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  <img src="https://img.shields.io/badge/Author-SmartMatt-blue" />
</p>

## Overview
The board below represents the initial state of the game. Symbol `|ф>` represents the superposition state! The user always has the option to make the first move. Signs `[0>` and `|1>` represent the figures chosen by the computer and the user respectively. However, unlike the classic tic tac toe, there is no 100% probability that when the computer/user make their move, it will result in a corresponding move. For example, if the user selects a figure, it is possible that it will take the value `|0>` instead of `|1>`. This is the effect of quantum superposition in the game Quantum Tic Tac Toe!

|   | 0 | 1 | 2 | 
| - | - | - | - |
| 0 | ψ | ψ | ψ |
| 1 | ψ | ψ | ψ |
| 2 | ψ | ψ | ψ |

## Installation
Install Quantum Tic-Tac-Toe with pip

```bash
  python -m venv venv
  venv\Scripts\activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  streamlit run app.py
```
    
## Screenshots
![Game](https://smartmatt.pl/github/quantum-tic-tac-toe/quantum-tic-tac-toe-game.png)
*The main screen of the game.*

![Winning](https://smartmatt.pl/github/quantum-tic-tac-toe/quantum-tic-tac-toe-won.png)
*Screen and effects displayed after winning a game*

![Loosing](https://smartmatt.pl/github/quantum-tic-tac-toe/quantum-tic-tac-toe-lose.png)
*Screen and effects displayed after loosing a game*
