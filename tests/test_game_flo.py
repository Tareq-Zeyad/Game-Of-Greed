import pytest

from tests.flow.flo import Flo

from game_of_greed.game import Game

pytestmark = [pytest.mark.flow]


# def test_quitter():
#     game = Game()
#     diffs = Flo(game.play, path="tests/flow/quitter.sim.txt")
#     assert not diffs, diffs


# def test_one_and_done():
#     game = Game()
#     diffs = Flo(game.play, path="tests/flow/one_and_done.sim.txt")
#     assert not diffs, diffs


# def test_single_bank():
#     game = Game()
#     diffs = Flo(
#         game.play, path="tests/flow/bank_one_roll_then_quit.sim.txt"
#     )
#     assert not diffs, diffs


def test_bank_first_for_two_rounds():

    Flo.test('tests/flow/bank_first_for_two_rounds.sim.txt')
    # game = Game()
    # diffs = Flo(
    #     game.play, path="tests/flow/bank_first_for_two_rounds.sim.txt"
    # )
    # assert not diffs, diffs
