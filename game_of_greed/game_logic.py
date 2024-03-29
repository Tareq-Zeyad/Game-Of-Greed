from collections import Counter
import random
from typing import List


Scores = {"Straight": 1500,    "Three Pairs":	1500,
          (1, 1): 100,    (1, 2): 200,    (1, 3): 1000,    (1, 4): 2000,    (1, 5): 3000,    (1, 6): 4000,
          (2, 3): 200,    (2, 4): 400,    (2, 5): 600,    (2, 6): 800,
          (3, 3): 300,    (3, 4): 600,    (3, 5): 900,    (3, 6): 1200,
          (4, 3): 400,    (4, 4): 800,    (4, 5): 1200,    (4, 6): 1600,
          (5, 1): 50,    (5, 2): 100,    (5, 3): 500,    (5, 4): 1000,    (5, 5): 1500,    (5, 6): 2000,
          (6, 3): 600,    (6, 4): 1200,    (6, 5): 1800,    (6, 6): 2400
          }


class GameLogic:
    """
    Handle the logic of game of greed.
    Methods:
    1- Calculate Score(Static Method)
    Input = The input to calculate_score is a tuple of integers that represent a dice roll.

    Output = The output from calculate_score is an integer representing the roll’s score according to rules of game.

    2- roll_dice(static Method)
    Input = The input to roll_dice is an integer between 1 and 6
    Output = The output of roll_dice is a tuple with random values between 1 and 6.


    """

    def __init__(self, dice_num=6):
        self.dice_num = dice_num

    @staticmethod
    def roll_dice(dice_num=6):
        return tuple(random.randint(1, 6) for _ in range(0, dice_num))

    @staticmethod
    def calculate_score(dice):
        score = 0
        dices = Counter(dice)
        x = list(dices)
        x.sort()
        if x == [1, 2, 3, 4, 5, 6]:
            score += Scores["Straight"]
        elif list(dices.values()) == [2, 2, 2]:

            score += Scores["Three Pairs"]

        else:
            for i in dices.items():
                try:
                    score += Scores[i]
                except:
                    score += 0
        return score

    @staticmethod
    def get_scorers(_input):
        keep_points_tuple = [int(i) for i in _input]
        all_dices_score = GameLogic.calculate_score(keep_points_tuple)
        if all_dices_score == 0:
            return ()
        else:
            list_of_scorers = []
        _input = list(_input)
        for i in range(len(_input)):
            roll = _input[:i] + _input[i + 1:]
            score = GameLogic.calculate_score(roll)
            if score != all_dices_score:
                list_of_scorers.append(_input[i])
                return tuple(list_of_scorers)

    @staticmethod
    def validate_keepers(roll, keepers):
        _rolled_dice = list(roll)
        _input = [int(i) for i in keepers]

        if len(_input) > len(_rolled_dice):
            return False
        for i in _input:
            if i in _rolled_dice:
                _rolled_dice.remove(i)
            else:
                return False

        return True


if __name__ == "__main__":
    print(GameLogic.calculate_score((4, 3, 2, 2, 5, 6)))
    print(GameLogic.calculate_score((4, 4, 5, 5, 2, 2)))
    print(GameLogic.calculate_score((4, 3, 2, 1, 5, 6)))
    print(GameLogic.calculate_score((2, 2, 2, 4, 4, 4)))
    print(GameLogic.calculate_score((3, 3, 3, 1, 1, 1)))
