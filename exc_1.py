class PlaneException(Exception):
    def __init__(self,current_location,destination_location,fuel,min_fuel):
        self.current_location = current_location
        self.destination_location = destination_location
        self.current_fuel = fuel
        self.min_fuel_needed = min_fuel
    def __str__(self):
        print(f"Current Location: {self.current_location[0]}:{self.current_location[1]}")
        print(f"Destination Location: {self.destination_location[0]}:{self.destination_location[1]}")
        print(f"Fuel we have: {self.current_fuel}")
        print(f"Minimum fuel we need: {self.min_fuel_needed}")
           

class Plane(Exception):

    def __init__(self,x,y,fuel) :
        self.current_location = [x,y]
        self.destination_location = []
        self.current_location[x] = y
        self.fuel = fuel
        self.distance = 0

    def get_plane_location(self):
        return f"Location: {self.current_location}"

    def get_plane_fuel(self):
        return f"Current Fuel Is:  {self.fuel}"

    def add_fuel(self, value=0):
        self.fuel += value

    def total_kilometers(self, x2, y2):
        return abs(abs(x2) - abs(self.current_location[0])) + abs(abs(self.current_location[1]) - + abs(y2))

    def fly(self, x2, y2):
        self.destination_location = [x2, y2]
        kilometers = self.total_kilometers(x2,y2)
        total_fuel_needed = kilometers * 4
        minimum_fuel_needed = total_fuel_needed - self.fuel

        if total_fuel_needed > self.fuel:
            raise(PlaneException(self.current_location,self.destination_location,self.fuel,minimum_fuel_needed))
           
        
        print("The amount of fuel: ", self.fuel)
        print("The amount of used fuel: ", kilometers * 4)
        print("The coverd distance: ", kilometers * 4)
        print ("The remaining fuel: ", self.get_fuel()- kilometers * 4)
    

    def __str__(self):
        print("Current Location: ", self.get_plam_location())
        print("Fuel: ", self.fuel())
        print(self.fly())

if __name__ == '__main__':
    plane_1 = Plane(0,0,22)
    plane_1.fly(3,4)
    plane_1.add_fuel(10)
    plane_1.fly(10,10)
    plane_1.fly(3,5)
