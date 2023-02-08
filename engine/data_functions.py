import chess
import numpy as np


def split_dims(board):
  # this is the 3d matrix
  board3d = np.zeros((14, 8, 8), dtype=np.int8)

  # here we add the pieces's view on the matrix
  for piece in chess.PIECE_TYPES:
    for square in board.pieces(piece, chess.WHITE):
      idx = np.unravel_index(square, (8, 8))
      board3d[piece - 1][7 - idx[0]][idx[1]] = 1
    for square in board.pieces(piece, chess.BLACK):
      idx = np.unravel_index(square, (8, 8))
      board3d[piece + 5][7 - idx[0]][idx[1]] = 1

  # add attacks and valid moves too
  # so the network knows what is being attacked
  aux = board.turn
  board.turn = chess.WHITE
  for move in board.legal_moves:
      i, j = square_to_index(move.to_square)
      board3d[12][i][j] = 1
  board.turn = chess.BLACK
  for move in board.legal_moves:
      i, j = square_to_index(move.to_square)
      board3d[13][i][j] = 1
  board.turn = aux

  return board3d


def square_to_index(square):
  squares_index = {'a': 0,
                   'b': 1,
                   'c': 2,
                   'd': 3,
                   'e': 4,
                   'f': 5,
                   'g': 6,
                   'h': 7}
                   
  letter = chess.square_name(square)
  return 8 - int(letter[1]), squares_index[letter[0]]