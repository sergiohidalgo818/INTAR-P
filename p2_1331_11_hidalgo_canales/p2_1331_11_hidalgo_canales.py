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
            contx+=1

      totals.append(contx+conty)
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
    countx=0
    keys = state.board.keys()

    t1 = self.get_max_tokens(state, token, keys)
    t2 = self.get_max_tokens(state, nottoken, keys)

    
    res =  t2[1] - t1[0]
    
    
    return res

'''
class Solution1(StudentHeuristic):
  def get_name(self) -> str:
    return "Thanker Nombert"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    # let's use an auxiliary function
    aux = self.dummy(123)
    return aux

  def dummy(self, n: int) -> int:
    return n + 1

class Solution2(StudentHeuristic):
  def get_name(self) -> str:
    return "Thanker Nombert"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    # let's use a global function
    return func_glob(2, state)
'''