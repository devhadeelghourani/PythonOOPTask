from exc_1 import Plane


class Concorde(Plane):
    def __init__(self, x: int, y: int, fuel: float) -> object:
        super().__init__(x, y, fuel)
    
    def validate_passengers_number(self, passengers: int) -> int:
        """_summary_
        Check if the passengers number is valid or not.
        No negative or zero numbers, and not greater than 15.
        
        Args:
            passengers (int): passengers number

        Raises:
            ValueError: _description_

        Returns:
            int: passengers number
        """
        
        if not -1 < passengers < 16:
            raise ValueError("Number of passengers not valid!") 
        else:
            return passengers
    
    def fly(self, x2: int, y2: int, passengers: int) -> None:
        """summary:
        * Main Goal: print put the flight details.
        
        * Needs the coordinates of currnet location, destination location
          and passengers numbers.
        * check if the fuel in enough for the flight
          using the fuel_shortage_flage.  
        * Check if the passengers number is valid.
        * And finaly, since every thing is okay, it prints 
          the details of the flight.    
           

        Args:
            x2 (int): X-coordinate of the destination
            y2 (int): Y-coordinate of the destination
            passengers (int, optional):passengers number and the defualt = 0.
        """
        try:
            passengers = self.validate_passengers_number(passengers)
        except Exception as e:
            print(e)
        else:
            super().fly(x2, y2, passengers)
        
    def fastest_plane(self, planes: dict) -> object:
        """_summary_
        looping throgh list of planes and find the fastest one.

        Args:
            planes (dict): list of dictionary of planes

        Returns:
            object: plane which is the fastest
        """
        fastest = 0
        return map(lambda plane: fastest > plane.get_distance(self.x2, self.y2)
                   or fastest == 0, planes)
               
        
plane_2 = Concorde(1, 0, 20)
try:
    plane_2.fly(10, 10, 5)
except Exception as e:
    print(e)
    
try:
    plane_2.fly(4, 3, 3)
except Exception as e:
    print(e)
    
plane_2.add_fuel(35)
try:
    print(plane_2.get_plane_fuel())
except Exception as e:
    print(e)
try:
    plane_2.fly(5, 3, 3)
except Exception as e:
    print(e)
