class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parkMap = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        self.parkMap[carType - 1] -= 1
        return self.parkMap[carType - 1] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)