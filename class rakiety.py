"""
from random import randint


class Rocket:
    def __init__(self):
        self.altitude = 0

    def moveUp(self):
        self.altitude += randint(1, 5)


rockets = [Rocket() for _ in range(5)]

for _ in range(10):
    rocketIndex = randint(0, 4)
    rockets[rocketIndex].moveUp()

for rocket in rockets:
    print('Rakieta osiągnęła wysokość', rocket.altitude)
"""


from random import randint

class Rocket:
    def __init__(self):
        self.altitude = 0

    def moveUp(self):
        self.altitude += 1

rockets = [Rocket() for _ in range(5)]

for _ in range (10):
    rocketIndex = randint(0, 4)
    rockets[rocketIndex].moveUp()

for rocket in rockets:
    print(rocket.altitude)
