import numpy as np

from typing import Sequence

from reversi import from_dictionary_to_array_board

from game import (
    TwoPlayerGameState,
)

from tournament import (
    StudentHeuristic,
)


def simple_evaluation_function(state: TwoPlayerGameState) -> float:
    """Return a random value, except for terminal game states."""
    state_value = 2*np.random.rand() - 1

    if state.end_of_game:
        scores = state.scores
        # Evaluation of the state from the point of view of MAX

        assert isinstance(scores, (Sequence, np.ndarray))
        score_difference = scores[0] - scores[1]

        if state.is_player_max(state.player1):
            state_value = score_difference
        elif state.is_player_max(state.player2):
            state_value = - score_difference
        else:
            raise ValueError('Player MAX not defined')

    return state_value

def func_glob(n: int, state: TwoPlayerGameState) -> float:
  return n + simple_evaluation_function(state)

class Solution1(StudentHeuristic):
  def get_name(self) -> str:
    return "Thanker Nombert1"
  
  def get_max_tokens(self, state:TwoPlayerGameState, token, keys):
    totals = list()
    listx = list()
    listx.append(0)
    listy = list()
    listy.append(0)

    h = state.game.height
    w = state.game.width

    for i in state.board:
      contx =0
      conty =0
      t = tuple(i)

      if t[0] not in listx:
        for j in range(t[1], w):
          taux = (t[0], j)
          if taux in keys and state.board[taux] != token:
            listx.append(t[0])
            contx+=1

      if t[1] not in listy:
        for j in range(t[0], h):
          taux = (j, t[1])
          if taux in keys and state.board[taux] != token:
            listx.append(t[0])
            conty+=1


      totals.append(contx)
      totals.append(conty)
    totals.sort(reverse=True)
    return totals
  
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    aux = 1
    # player 1 B player 2 W
    if state.is_player_max(state.player1):
      token = 'B'
      nottoken = 'W'
    elif state.is_player_max(state.player2):
      token = 'W'
      nottoken = 'B'
    else:
      raise ValueError('Player MAX not defined')
    


    # number of tokens he can eat - number of tokens we can eat
    keys = state.board.keys()

    t1 = self.get_max_tokens(state, token, keys)
    t2 = self.get_max_tokens(state, nottoken, keys)

    
    res =  t2[0] - t1[0]
    
    
    return res
  
class Solution2(StudentHeuristic):
  def get_name(self) -> str:
    return "Thanker Nombert2"
  
  def get_max_tokens(self, state:TwoPlayerGameState, token):

    board = from_dictionary_to_array_board(state.board, state.game.height, state.game.width)

    count = 0

    for row in board:
      for square in row:
        if square == token:
          count += 1

    return count
  
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    # player 1 B player 2 W
    if state.is_player_max(state.player1):
      token = 'B'
      nottoken = 'W'
    elif state.is_player_max(state.player2):
      token = 'W'
      nottoken = 'B'
    else:
      raise ValueError('Player MAX not defined')
    
    # number of tokens max has - number of tokens min has

    max_tokens = self.get_max_tokens(state, token)
    min_tokens = self.get_max_tokens(state, nottoken)

    res =  max_tokens - min_tokens
    
    return res
  
class Solution3(StudentHeuristic):
  def get_name(self) -> str:
    return "Thanker Nombert3"
  
  def get_max_tokens(self, state:TwoPlayerGameState, token, nottoken):

    board = from_dictionary_to_array_board(state.board, state.game.height, state.game.width)

    count = 0

    for idx, row in enumerate(board):
      for idy, square in enumerate(row):
        if square == token:

          if (idx == 0 and idy == 0):
            for index, aux_row in enumerate(reversed(board)):
              aux_count = 0
              if aux_row[0] == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_row[0] == token:
                aux_count += 1
              else:
                count += (2 * ((len(board) - index) + aux_count))
                break
            for index, aux_square in enumerate(reversed(row)):
              aux_count = 0
              if aux_square == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_square == token:
                aux_count += 1
              else:
                count += (2 * ((len(row) - index) + aux_count))
                break
            for index, aux_row in reversed(list(enumerate(board))):
              aux_count = 0
              if aux_row[index] == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_row[index] == token:
                aux_count += 1
              else:
                count += (2 * ((len(board) - index) + aux_count))
                break
            count -= 4

          elif (idx == 0 and idy == (len(row)-1)):
            for index, aux_row in enumerate(reversed(board)):
              aux_count = 0
              if aux_row[len(row)-1] == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_row[len(row)-1] == token:
                aux_count += 1
              else:
                count += (2 * ((len(board) - index) + aux_count))
                break
            for index, aux_square in enumerate(row):
              aux_count = 0
              if aux_square == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_square == token:
                aux_count += 1
              else:
                count += (2 * ((len(row) - index) + aux_count))
                break
            for index, aux_row in enumerate(reversed(board)):
              aux_count = 0
              if aux_row[index] == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_row[index] == token:
                aux_count += 1
              else:
                count += (2 * ((len(board) - index) + aux_count))
                break
            count -= 4

          elif (idx == (len(board)-1) and idy == 0):
            for index, aux_row in enumerate(board):
              aux_count = 0
              if aux_row[0] == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_row[0] == token:
                aux_count += 1
              else:
                count += (2 * ((len(board) - index) + aux_count))
                break
            for index, aux_square in enumerate(reversed(row)):
              aux_count = 0
              if aux_square == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_square == token:
                aux_count += 1
              else:
                count += (2 * ((len(row) - index) + aux_count))
                break
            for index, aux_row in enumerate(board):
              aux_count = 0
              if aux_row[len(aux_row) - (index+1)] == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_row[len(aux_row) - (index+1)] == token:
                aux_count += 1
              else:
                count += (2 * ((len(board) - index) + aux_count))
                break
            count -= 4

          elif (idx == (len(board)-1) and idy == (len(row)-1)):
            for index, aux_row in enumerate(board):
              aux_count = 0
              if aux_row[len(row)-1] == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_row[len(row)-1] == token:
                aux_count += 1
              else:
                count += (2 * ((len(board) - index) + aux_count))
                break
            for index, aux_square in enumerate(row):
              aux_count = 0
              if aux_square == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_square == token:
                aux_count += 1
              else:
                count += (2 * ((len(row) - index) + aux_count))
                break
            for index, aux_row in enumerate(board):
              aux_count = 0
              if aux_row[index] == nottoken:
                if aux_count > 0:
                  aux_count += 1
                continue
              elif aux_row[index] == token:
                aux_count += 1
              else:
                count += (2 * ((len(board) - index) + aux_count))
                break
            count -= 4
          
          elif (idx == 1 and idy == 0) or (idx == 0 and idy == 1) or (idx == 1 and idy == 1):
            istoken = board[0][0]
            if istoken == token:
              count += 3
            elif istoken == nottoken:
              count += 2
            else:
              count += 1
          elif (idx == 1 and idy == (len(row)-1)) or (idx == 0 and idy == (len(row)-2)) or (idx == 1 and idy == (len(row)-2)):
            istoken = board[0][(len(row)-1)]
            if istoken == token:
              count += 3
            elif istoken == nottoken:
              count += 2
            else:
              count += 1
          elif (idx == (len(board)-2) and idy == 0) or (idx == (len(board)-1) and idy == 1) or (idx == (len(board)-2) and idy == 1):
            istoken = board[(len(board)-1)][0]
            if istoken == token:
              count += 3
            elif istoken == nottoken:
              count += 2
            else:
              count += 1
          elif (idx == (len(board)-2) and idy == (len(row)-1)) or (idx == (len(board)-1) and idy == (len(row)-2)) or (idx == (len(board)-2) and idy == (len(row)-2)):
            istoken = board[(len(board)-1)][(len(row)-1)]
            if istoken == token:
              count += 3
            elif istoken == nottoken:
              count += 2
            else:
              count += 1
          
          else:
            count += 2
            

    return count
  
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    # player 1 B player 2 W
    if state.is_player_max(state.player1):
      token = 'B'
      nottoken = 'W'
    elif state.is_player_max(state.player2):
      token = 'W'
      nottoken = 'B'
    else:
      raise ValueError('Player MAX not defined')
    
    # number of tokens max has - number of tokens min has

    max_tokens = self.get_max_tokens(state, token, nottoken)
    min_tokens = self.get_max_tokens(state, nottoken, token)

    res =  max_tokens - min_tokens
    
    return res