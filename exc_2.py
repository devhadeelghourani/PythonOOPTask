from exc_1 import Plane
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

        print(fuel_needed, self.fuel) 
        print (kilometers)

        if fuel_needed > self.fuel:
            print ("Current FUEL is not enough")
        else:
            print("The amount of used fuel: ", kilometers * 4)
            print("The coverd distance: ", kilometers * 4)
            print ("The remaining fuel: ", self.fuel - kilometers * 4)

    


plane_2 = Concorde(1,0,20)
plane_2.fly(10,10,5)
plane_2.fly(4,3,3)
plane_2.add_fuel(35)
print(plane_2.get_plane_fuel())
plane_2.fly(5,3,3)

