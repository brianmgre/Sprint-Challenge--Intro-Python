# To the GroundVehicle class, add method drive() that returns "vroooom".


class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # TODO

    def drive(self):
        return('vrooom')


# Subclass Motorcycle from GroundVehicle.

# TODO

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels)

    def drive(self):
        return('BRAAAP!!')


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

for vehicle in vehicles:
    print(vehicle.drive())
