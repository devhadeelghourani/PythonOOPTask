from dis import dis
from exc_1 import FuelShortage, Plane
class Concorde(Plane):
    def __init__(self,x,y,fuel):
        super().__init__(x,y,fuel)
        self.number_of_passenger = self.passengers_number(0)
    
    def passengers_number(self, passengers):
        if not -1 < passengers < 16:
            raise ValueError("Number of passengers not valid!") 
        else:
            return passengers
    
    def fly(self, x2, y2, passengers):
        try:
            passengers = self.passengers_number(passengers)
        except Exception as e:
            print(e)
        else:
            super().fly(x2, y2, passengers)
        
    def fastest_plane(self, planes):
        fastest = 0
        return map(lambda plane : fastest > plane.get_distance() or fastest==0 , planes)        
        

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
