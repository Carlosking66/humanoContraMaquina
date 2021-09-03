#!/usr/bin/env python3
# Código original: Ramón Gª Magadán 2021
# Adds: Carlos Menéndez

import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish")
board = chess.Board()

def InputMove():
    # * Carlos Menéndez - Sep  2021
    # Filtra la entrada de jugadas del usuario.
    global board # Se movera en el objeto tablero global.
    strMove = "Nothing"    
    
    strMove = input("Your Tourn: ")
    # Limitar longitud a 4 ó 5    
    if len(strMove) < 4:
        strMove = strMove + "    "
        #print(strMove + "Se han agregado 4 sps")
    if len(strMove) > 5:
        strMove = strMove[0:5]
        #print("la  longitud se ha truncado!")

   #Comprobar que la jugada  está en el conjunto de posibles.
    if not(chess.Move.from_uci(strMove) in board.legal_moves):
        strMove = "Atention!!. Your move " + strMove + " is not legal now  er!."
        print(strMove)
        print("Please, try again!. - Remember to use the long notation (d2d4).")
        strMove = InputMove()  # Llamada recursiva hasta  recibir jugada legal
    return(strMove)        

print("Welcome to your challenge  against Stockfish!!")
print("Enter your moves in the format: d2d4 (algebraic long notation).")
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    print(result.move)
    strMove = InputMove()    
    board.push_san(strMove)
        
engine.quit()
print(board)
print("Game Over - * R.G.Magadan 2021")
