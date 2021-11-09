# import pytest
# from tests.flow import flo
# from game_of_greed.game_logic import 


# pytestmark = [pytest.mark.flow]




# def test_hot_dice():
#     """When all dice are used without a zilch
#     then user gets 6 fresh dice and continues turn.
#     """
#     diffs = flo(Game().play, path="tests/folw/hot_dice.sim.txt")
#     assert not diffs, diffs


# def test_cheat_and_fix():
#     """Cheating (or typos) should not be allowed.
#     Therefore the user's input must be validated
#     If invalid prompt user for re-entry
#     """

#     diffs = flo(Game().play, path="tests/folw/cheat_and_fix.sim.txt")
#     assert not diffs, diffs


# def test_zilcher():
#     """
#     No scoring dice results in a 'zilch'
#     which wipes away shelved points
#     and ends turn
#     """

#     diffs = flo(Game().play, path="tests/folw/zilcher.sim.txt")
#     assert not diffs, diffs