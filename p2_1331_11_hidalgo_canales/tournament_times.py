"""Illustration of tournament but saves times from execution (with timeit).

Authors:
    Alejandro Bellogin <alejandro.bellogin@uam.es>
Modified by:
        Sergio Hidalgo <sergio.hidalgo@estudiante.uam.es>
"""

from __future__ import annotations  # For Python 3.7
from p2_1331_11_hidalgo_canales import Solution1

import numpy as np

from game import Player, TwoPlayerGameState, TwoPlayerMatch
from heuristic import simple_evaluation_function
from reversi import (
    Reversi,
    from_array_to_dictionary_board,
    from_dictionary_to_array_board,
)
from tournament_selectstr import StudentHeuristic, Tournament
from strategy import MinimaxAlphaBetaStrategy, MinimaxStrategy
import timeit
import json


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

    initial_board = None  # np.zeros((dim_board, dim_board))
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


dictionary = dict()

code = """tour = Tournament(max_depth=3, init_match=create_match)
strats = {'opt1': [Heuristic1], 'opt1': [Solution1]}

n = 1

tour.run(student_strategies=strats, increasing_depth=False, n_pairs=n,
         allow_selfmatch=False, strategy_sel=MinimaxStrategy)"""
imports = """from __main__ import Tournament, create_match, Heuristic1, Heuristic2, Heuristic3, Solution1, MinimaxStrategy"""
dictionary['timesminmax1'] = timeit.timeit(
    code, imports)

code = """tour = Tournament(max_depth=3, init_match=create_match)
strats = {'opt1': [Heuristic2], 'opt1': [Solution1]}

n = 1

tour.run(student_strategies=strats, increasing_depth=False, n_pairs=n,
         allow_selfmatch=False, strategy_sel=MinimaxStrategy)"""
imports = """from __main__ import Tournament, create_match, Heuristic1, Heuristic2, Heuristic3, Solution1, MinimaxStrategy"""
dictionary['timesminmax2'] = timeit.timeit(
    code, imports)

code = """tour = Tournament(max_depth=3, init_match=create_match)
strats = {'opt1': [Heuristic3], 'opt1': [Solution1]}

n = 1

tour.run(student_strategies=strats, increasing_depth=False, n_pairs=n,
         allow_selfmatch=False, strategy_sel=MinimaxStrategy)"""
imports = """from __main__ import Tournament, create_match, Heuristic1, Heuristic2, Heuristic3, Solution1, MinimaxStrategy"""
dictionary['timesminmax3'] = timeit.timeit(
    code, imports)

code = """tour = Tournament(max_depth=3, init_match=create_match)
strats = {'opt1': [Heuristic1], 'opt1': [Solution1]}

n = 1

tour.run(student_strategies=strats, increasing_depth=False, n_pairs=n,
         allow_selfmatch=False, strategy_sel=MinimaxAlphaBetaStrategy)"""
imports = """from __main__ import Tournament, create_match, Heuristic1, Heuristic2, Heuristic3, Solution1, MinimaxAlphaBetaStrategy"""
dictionary['timesminmaxab1'] = timeit.timeit(
    code, imports)

code = """tour = Tournament(max_depth=3, init_match=create_match)
strats = {'opt1': [Heuristic2], 'opt1': [Solution1]}

n = 1

tour.run(student_strategies=strats, increasing_depth=False, n_pairs=n,
         allow_selfmatch=False, strategy_sel=MinimaxAlphaBetaStrategy)"""
imports = """from __main__ import Tournament, create_match, Heuristic1, Heuristic2, Heuristic3, Solution1, MinimaxAlphaBetaStrategy"""
dictionary['timesminmaxab2'] = timeit.timeit(
    code, imports)

code = """tour = Tournament(max_depth=3, init_match=create_match)
strats = {'opt1': [Heuristic3], 'opt1': [Solution1]}

n = 1

tour.run(student_strategies=strats, increasing_depth=False, n_pairs=n,
         allow_selfmatch=False, strategy_sel=MinimaxAlphaBetaStrategy)"""
imports = """from __main__ import Tournament, create_match, Heuristic1, Heuristic2, Heuristic3, Solution1, MinimaxAlphaBetaStrategy"""
dictionary['timesminmaxab3'] = timeit.timeit(
    code, imports)




json_object = json.dumps(dictionary, indent=4)

with open("data.json", "w") as outfile:
    outfile.write(json_object)
