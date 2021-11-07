class Banker:
    """
    Description:
    A class to handle the points in game of greed.
    Methods:
    1- shelf (instance method): 
    Input = the amount of points (integer) to add to shelf.
    shelf should temporarily store unbanked points.
    2- bank(instance method):
    should add any points on the shelf to total and reset shelf to 0.
    3- clear_shelf (instance method):
    Reset shelf to 0.
    """

    def __init__(self):
        self.shelved = 0
        self. balance = 0

    def shelf(self, points: int):
        self.shelved += points
        return self.shelved

    def clear_shelf(self):
        self.shelved = 0

    def bank(self):
        self.balance += self.shelved
        self.clear_shelf()
        return self.balance
