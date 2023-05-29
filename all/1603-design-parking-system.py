'''
2023/05/29 daily challenge
'''

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # remaining parking spaces
        self.space = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.space[carType]:
            # there's space available, park the car.
            self.space[carType] -= 1
            return True
        
        # no more space available for the carType.
        return False

