import pytest

from tests.flow.flo import Flo

from game_of_greed.game import Game

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
