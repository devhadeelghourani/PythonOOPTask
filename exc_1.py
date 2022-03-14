class FuelShortage(Exception):
    def __init__(self, current_location, destination_location, fuel, min_fuel):
        self.current_location = current_location
        self.destination_location = destination_location
        self.current_fuel = fuel
        self.min_fuel_needed = min_fuel
        msg = "\nCurrent Location: "\
            f"{current_location[0]}:{current_location[1]}\n"\
            "Destination Location: "\
            f"{destination_location[0]}:{destination_location[1]}" \
            f"\nFuel we have: {self.current_fuel}\n"\
            f"Minimum fuel we need: {self.min_fuel_needed}\n"
        super().__init__(msg)


class Plane(Exception):
    def __init__(self, x, y, fuel):
        self.current_location = [x, y]
        self.destination_location = []
        self.fuel = fuel
        self.distance = 0

    def get_plane_location(self):
        return f"Location: {self.current_location}"

    def get_plane_fuel(self):
        return f"Current Fuel Is:  {self.fuel}"

    def add_fuel(self, value=0):
        self.fuel += value

    def get_distance(self, x2, y2):
        return abs(abs(x2) + abs(self.current_location[0])) + \
            abs(abs(self.current_location[1]) + abs(y2))

    def fly(self, x2, y2):
        self.destination_location = [x2, y2]
        distance = self.get_distance(x2, y2)
        fuel_needed = distance * 4
        minimum_fuel_needed = fuel_needed - self.fuel

        if fuel_needed > self.fuel:
            raise(FuelShortage(self.current_location,
                               self.destination_location, 
                               self.fuel, minimum_fuel_needed))
        else:
            print("The amount of fuel: ", self.fuel)
            print("The amount of used fuel: ", distance * 4)
            print("The coverd distance: ", distance * 4)
            print("The remaining fuel: ", self.fuel - distance * 4)

    def __str__(self):
        print("Current Location: ", self.get_plane_location())
        print("Fuel: ", self.fuel)

if __name__ == '__main__':
    plane_1 = Plane(0, 0, 22)
    try:
        plane_1.fly(3, 4)
    except Exception as e:
        print(e)
    plane_1.add_fuel(10)
    try:
        plane_1.fly(10, 10)
    except Exception as e:
        print(e)
    plane_1.fly(3, 5)
