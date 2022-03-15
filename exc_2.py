from exc_1 import FuelShortage, Plane
class Concorde(Plane):
    def __init__(self,x,y,fuel):
        super().__init__(x,y,fuel)
        self.number_of_passenger = self.passengers_number(0)
    
    def passengers_number(self, passengers):
        if not -1 < passengers < 16:
            raise ValueError("Number of passengers not valid!") 
    
    def fly(self, x2, y2, passengers_number):
        self.destination_location = [x2, y2]
        kilometers = self.get_distance(x2,y2)
        if passengers_number == 0:
            fuel_needed = kilometers * 4
        elif 0 < passengers_number < 8:
            fuel_needed = kilometers * 7
        else:
            fuel_needed = kilometers * 9

        if fuel_needed > self.fuel:
            min_fuel = fuel_needed - self.fuel
            raise(FuelShortage(self.current_location, self.destination_location, self.fuel, min_fuel))
        else:
            print("The amount of used fuel: ", kilometers * 4)
            print("The coverd distance: ", kilometers * 4)
            print ("The remaining fuel: ", self.fuel - kilometers * 4)
        
    def fastest_plane(self, planes):
        fastest = 0
        return map(lambda plane : fastest > plane.get_distance(), planes)        
        

plane_2 = Concorde(1,0,20)
try:
    plane_2.fly(10,10,5)
except Exception as e:
    print(e)
    
try:
    plane_2.fly(4,3,3)
except Exception as e:
    print(e)
    
plane_2.add_fuel(35)
try:
    print(plane_2.get_plane_fuel())
except Exception as e:
    print(e)
try:
    plane_2.fly(5,3,3)
except Exception as e:
    print(e)
