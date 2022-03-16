class FuelShortage(Exception):
    def __init__(self, current_location, destination_location, current_fuel, min_fuel):
        msg = "\nCurrent Location: "\
            f"{current_location[0]}:{current_location[1]}\n"\
            "Destination Location: "\
            f"{destination_location[0]}:{destination_location[1]}" \
            f"\nFuel we have: {current_fuel}\n"\
            f"Minimum fuel we need: {min_fuel}\n"
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

    def get_distance(self, x2, y2):
        return abs(abs(x2) + abs(self.current_location[0])) + \
            abs(abs(self.current_location[1]) + abs(y2))

    def add_fuel(self, value=0):
        self.fuel += value

    def minimum_fuel_needed(self, distance, passengers):
        if passengers == 0:
            return distance * 4
        elif 0 < passengers < 8:
            return distance * 7
        else:
            return distance * 9
        

    def fight_data(self, fuel, distance, remained_fuel):
        print("The amount of fuel: ", fuel)
        print("The amount of used fuel: ", distance * 4)
        print("The coverd distance: ", distance)
        print("The remaining fuel: ", remained_fuel)

    def fly(self, x2, y2, passengers):
        self.destination_location = [x2, y2]
        distance = self.get_distance(x2, y2)
        fuel_needed = self.minimum_fuel_needed(distance,0)
                
        fuel_shortage_flag = fuel_needed > self.fuel
        if fuel_shortage_flag:
            required_fuel = fuel_needed - self.fuel
            raise(FuelShortage(self.current_location,
                               self.destination_location, 
                               self.fuel, required_fuel))
        else:
            remained_fuel = self.fuel - fuel_needed
            self.fight_data(self.fuel, distance, remained_fuel)
            
    def __str__(self):
        print("Current Location: ", self.get_plane_location())
        print("Fuel: ", self.fuel)

if __name__ == '__main__':
    plane_1 = Plane(0, 0, 22)
    try:
        plane_1.fly(3, 4, 0)
    except Exception as e: 
        print(e)
    plane_1.add_fuel(10)
    try:
        plane_1.fly(10, 10, 0)
    except Exception as e:
        print(e)
    plane_1.fly(3, 5, 0)
