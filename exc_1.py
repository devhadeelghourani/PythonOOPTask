class FuelShortage(Exception):
    def __init__(self, current_location: list, destination_location: list,
                 current_fuel: float, min_fuel: float):
        msg = "\nCurrent Location: "\
            f"{current_location[0]}:{current_location[1]}\n"\
            "Destination Location: "\
            f"{destination_location[0]}:{destination_location[1]}" \
            f"\nFuel we have: {current_fuel}\n"\
            f"Minimum fuel we need: {min_fuel}\n"
        super().__init__(msg)


class Plane(Exception):
    planes_number = 0

    def __init__(self, x: int, y: int, fuel: float) -> object:
        Plane.planes_number += 1
        self.current_location = [x, y]
        self.destination_location = []
        self.fuel = fuel
        self.distance = 0

    def get_plane_location(self) -> list:
        """
        Setting the current plane location, before taking off

        Returns:
            list: the cordinates of the current location [x, y]
        """
        return f"Location: {self.current_location}"

    def get_plane_fuel(self) -> float:
        """
        find the amount of fuel in the plane

        Returns:
            float: plane fuel
        """
        return f"Current Fuel Is:  {self.fuel}"

    def get_distance(self, x2: int, y2: int) -> int:
        """
        calculate destance of the trip
        Args:
            x2 (int): X-coordinate of the destination
            y2 (int): Y-coordinate of the destination

        Returns:
            int: destance between current location and destination
        """
        return abs(abs(x2) + abs(self.current_location[0])) + \
            abs(abs(self.current_location[1]) + abs(y2))

    def add_fuel(self, value: float):
        """
        enables us to increase the fuel with a spesific amount the user pass
        Args:
            value (float): amount of additional fuel

        """
        self.fuel += value

    def minimum_fuel_needed(self, distance: int, passengers: int) -> int:
        """
        calculate the minimum amount of plane
        fuel which we need to take off.
        Amount of fuel depends on two factors:
        1- flight distance
        2- passengers number

        Args:
            distance (int): flight distance
            passengers (int): passengers number on the flight

        Returns:
            int: minimum fuel needed to be added
        """
        if passengers == 0:
            return distance * 4
        elif 0 < passengers < 8:
            return distance * 7
        else:
            return distance * 9

    def fight_details(self, fuel: float, distance: int,
                      remaineded_fuel: float) -> None:
        """
        print out the flight details:
        1- Total fuel before the plane taking off.
        2- Fuel used through the trip
        3- Covered distance.
        4- Remained fuel after the flight

        Args:
            fuel (float): amount of fuel we have
            distance (int): covered distance of the flight
            remaineded_fuel (float): remained fuel after the flight
        """
        print("The amount of fuel: ", fuel)
        print("The amount of used fuel: ", distance * 4)
        print("The coverd distance: ", distance)
        print("The remaining fuel: ", remaineded_fuel)

    def fly(self, x2: int, y2: int, passengers: int = 0) -> None:
        """
        * Main Goal: print put the flight details.
        
        * Needs the coordinates of currnet location, destination location
          and passengers numbers.
        * checking if the fuel in enough for the flight
          using the fuel_shortage_flage.
        * And finaly, since every thing is okay, it prints
          the details of the flight.
        Args:
            x2 (int): X-coordinate of the destination
            y2 (int): Y-coordinate of the destination
            passengers (int, optional):passengers number and the defualt = 0.
        """
        self.destination_location = [x2, y2]
        distance = self.get_distance(x2, y2)
        fuel_needed = self.minimum_fuel_needed(distance, passengers)

        fuel_shortage_flag = fuel_needed > self.fuel
        if fuel_shortage_flag:
            required_fuel = fuel_needed - self.fuel
            raise(FuelShortage(self.current_location,
                               self.destination_location,
                               self.fuel, required_fuel))
        else:
            remained_fuel = self.fuel - fuel_needed
            self.fight_details(self.fuel, distance, remained_fuel)

    def __str__(self) -> None:
        """
        print out the plane current location and the fuel
        """
        print("Current Location: ", self.get_plane_location())
        print("Fuel: ", self.fuel)


if __name__ == '__main__':
    plane_1 = Plane(0, 0, 22)
    plane_2 = Plane(0, 0, 555)
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
    print(Plane.planes_number)
