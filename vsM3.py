#!/usr/bin/env python3
# Código original: Ramón Gª Magadán 2021
# Adds: Carlos Menéndez

import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish")
board = chess.Board()

def InputMove():
    # * Carlos Menéndez - Sep  2021
    # Comprueba   la entrada de jugadas del usuario.
    global board # Se movera en el objeto tablero global.
    strMove = "Nothing"    
    
    strMove = input("Your Tourn: ")
    strMove = board.parse_san(strMove)  #  Procesa SAN representation.
    # strMove pasa a ser class chess_move 
    #Comprobar que la jugada  está en el conjunto de posibles.
    if not strMove in board.legal_moves:
        strMove = "Atention!!. Your move " + strMove + " is not legal now here!."
        print(strMove)
        print("Please, try again!. - You can use the long notation (d2d4) if any ambiguity appears...")
        strMove = InputMove()  # Llamada recursiva hasta  recibir jugada legal
    return(strMove)        

print("Welcome to your challenge  against Stockfis chess moduleh!!")
print("Enter your moves in the format: d2d4 (algebraic long notation or d4 (SAN representation).")
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    print(result.move)
    strMove = InputMove()    
    board.push(strMove)
        
engine.quit()
print(board)
print("Game Over - * R.G.Magadan 2021")
