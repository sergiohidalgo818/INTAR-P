import numpy as np

from typing import Sequence

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
