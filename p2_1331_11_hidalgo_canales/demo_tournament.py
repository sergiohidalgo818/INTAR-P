"""Illustration of tournament.

Authors:
    Alejandro Bellogin <alejandro.bellogin@uam.es>

"""

from __future__ import annotations  # For Python 3.7
from p2_1331_11_hidalgo_canales import Solution1, Solution2, Solution3

import numpy as np

from game import Player, TwoPlayerGameState, TwoPlayerMatch
from heuristic import simple_evaluation_function
from reversi import (
    Reversi,
    from_array_to_dictionary_board,
    from_dictionary_to_array_board,
)
from tournament import StudentHeuristic, Tournament


class Heuristic1(StudentHeuristic):

    def get_name(self) -> str:
        return "dummy"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        # Use an auxiliary function.
        return self.dummy(123)

    def dummy(self, n: int) -> int:
        return n + 4


class Heuristic2(StudentHeuristic):

    def get_name(self) -> str:
        return "random"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        return float(np.random.rand())


class Heuristic3(StudentHeuristic):

    def get_name(self) -> str:
        return "heuristic"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        return simple_evaluation_function(state)


def create_match(player1: Player, player2: Player) -> TwoPlayerMatch:

    initial_board = None#np.zeros((dim_board, dim_board))
    initial_player = player1

    """game = TicTacToe(
        player1=player1,
        player2=player2,
        dim_board=dim_board,
    )"""

    initial_board = (
        ['..B.B..',
        '.WBBW..',
        'WBWBB..',
        '.W.WWW.',
        '.BBWBWB']
    )

    if initial_board is None:
        height, width = 8, 8
    else:
        height = len(initial_board)
        width = len(initial_board[0])
        try:
            initial_board = from_array_to_dictionary_board(initial_board)
        except ValueError:
            raise ValueError('Wrong configuration of the board')
        else:
            print("Successfully initialised board from array")

    game = Reversi(
        player1=player1,
        player2=player2,
        height=8,
        width=8
    )

    game_state = TwoPlayerGameState(
        game=game,
        board=initial_board,
        initial_player=initial_player,
    )

    return TwoPlayerMatch(game_state, max_seconds_per_move=1000, gui=False)


tour = Tournament(max_depth=3, init_match=create_match)

#tour = Tournament(max_depth=7, init_match=create_match)


# if the strategies are copy-pasted here:
strats = {'opt2': [Solution2], 'opt3': [Solution3], 'opt4' : [Solution1]}
# if the strategies should be loaded from files in a specific folder:
# folder_name = "folder_strat" # name of the folder where the strategy files are located
# strats = tour.load_strategies_from_folder(folder=folder_name, max_strat=3)

n = 1
scores, totals, names = tour.run(
    student_strategies=strats,
    increasing_depth=True,
    n_pairs=n,
    allow_selfmatch=False,
)

print(
    'Results for tournament where each game is repeated '
    + '%d=%dx2 times, alternating colors for each player' % (2 * n, n),
)

# print(totals)
# print(scores)

print('\ttotal:', end='')
for name1 in names:
    print('\t%s' % (name1), end='')
print()
for name1 in names:
    print('%s\t%d:' % (name1, totals[name1]), end='')
    for name2 in names:
        if name1 == name2 or name2 not in scores[name1]:
            print('\t---', end='')
        else:
            print('\t%d' % (scores[name1][name2]), end='')
    print()
