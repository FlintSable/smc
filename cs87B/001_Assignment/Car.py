#!/usr/bin/env python3

class Car():
    def __init__(self, engineType="Internal combustion engine", mileagePerGallon=0, zeroToSixty=0, fuelTank=0):
        self.engineType = engineType
        self.mileagePerGallon = mileagePerGallon
        self.zeroToSixty = zeroToSixty
        self.fuelTank = fuelTank
    
    def fillFuelTank(self):
        self.fuelTank = 100
        return self.fuelTank
    
    def retunTank(self):
        return self.fuelTank
    
    def __str__(self):
        return "(" + str(self.engineType) + ", " + str(self.mileagePerGallon) +  ", " + str(self.zeroToSixty) +  ", " + str(self.fuelTank)+")"


class VWGolf(Car):

    def __init__(self, engineType="Internal combustion engine", mileagePerGallon=24, zeroToSixty=6.7, fuelTank=100, make="VW", model="Golf"):
        super().__init__(engineType, mileagePerGallon, zeroToSixty, fuelTank)
        self.make = make
        self.model = model

    
    def __str__(self):
        return "(" + str(self.make) + ", " + str(self.model) + ", " +  str(self.engineType) + ", " + str(self.mileagePerGallon) +  ", " + str(self.zeroToSixty) +  ", " + str(self.fuelTank)+")"



def main():
    NewCar = Car()
    print(NewCar)

    VWCar = VWGolf(model="GTI Golf")
    print(VWCar)

if __name__ == "__main__":
    main()