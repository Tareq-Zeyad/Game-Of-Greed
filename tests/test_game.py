import pytest

from tests.flow.flo import Flo

from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic

pytestmark = [pytest.mark.flow]


def test_quitter():
    game = Game()
    diffs = Flo("tests/flow/quitter.sim.txt")
    # assert not diffs, diffs


def test_one_and_done():
    game = Game()
    diffs = Flo("tests/flow/one_and_done.sim.txt")
    # assert not diffs, diffs


def test_single_bank():
    game = Game()
    diffs = Flo("tests/flow/bank_one_roll_then_quit.sim.txt"
                )
    # assert not diffs, diffs


def test_bank_first_for_two_rounds():

    game = Game()
    diffs = Flo("tests/flow/bank_first_for_two_rounds.sim.txt"
                )
    # assert not diffs, diffs


def test_cheat_and_fix():
    """Cheating (or typos) should not be allowed.
    Therefore the user's input must be validated
    If invalid prompt user for re-entry
    """

    diffs = Flo(Game().play, path="tests/folw/cheat_and_fix.sim.txt")
    assert not diffs, diffs


def test_zilcher():
    """
    No scoring dice results in a 'zilch'
    which wipes away shelved points
    and ends turn
    """

    diffs = Flo(Game().play, path="tests/folw/zilcher.sim.txt")
    assert not diffs, diffs


def test_hot_dice():
    """When all dice are used without a zilch
    then user gets 6 fresh dice and continues turn.
    """
    diffs = Flo("tests/flow/hot_dice.txt")


def test_cheat_and_fix():
    """Cheating (or typos) should not be allowed.
    Therefore the user's input must be validated
    If invalid prompt user for re-entry
    """

    diffs = Flo("tests/flow/cheat_and_fix.sim.txt")


def test_zilcher():
    """
    No scoring dice results in a 'zilch'
    which wipes away shelved points
    and ends turn
    """

    diffs = Flo("tests/flow/zilch.sim.txt")


# @pytest.mark.parametrize(
#     "test_input,expected",
#     [
#         (tuple(), tuple()),
#         ((1,), (1,)),
#         ((1, 2), (1,)),
#         ((1, 2, 3), (1,)),
#         ((1, 2, 3, 5), (1, 5)),
#         ((5, 1, 2, 3), (1, 5)),
#         ((2, 3, 4), tuple()), ],)
# def test_get_scorers(test_input, expected):
#     actual = GameLogic.get_scorers(test_input)
#     assert sorted(actual) == sorted(expected)


def test_repeat_roller():
    """Allow setting aside scoring dice and rolling the rest    """
    diffs = Flo("tests/flow/repeat_roller.sim.txt")


def test_validate_legal_keepers():
    roll = (1, 2, 3, 4, 5)
    keepers = (5, 1)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = True
    assert actual == expected


def test_validate_illegal_keepers():
    roll = (1, 2, 3, 4, 5)
    keepers = (1, 1, 1, 1, 1)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = False
    assert actual == expected


def test_validate_illegal_overflow():
    roll = (1,)
    keepers = (1, 1, 1, 1, 1, 1)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = False
    assert actual == expected
