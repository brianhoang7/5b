# Author: Brian Hoang
# Date: 10/30/2019
# Description: creates a taxicab class that initializes taxicab's x coordinate, y coordinate, and odometer reading
#Has methods to take in movement instructions for taxicab in x and y direction and adds those values to odometer


#creates Taxicab class
class Taxicab:
    #__init__ method takes x,y coordinates as arguments
    def __init__(self,x_coord,y_coord):
        #initializes x,y,and odometer values
        self._x_coord=x_coord
        self._y_coord=y_coord
        self._odometer=0
    #method that is used to return x coord value
    def get_x_coord(self):
        return self._x_coord
    #method used to return y coord value
    def get_y_coord(self):
        return self._y_coord
    #method to return odometer value
    def get_odometer(self):
        return self._odometer
    #method to take in x direction movement and add total distance to odometer
    def move_x(self,xmove):
        #if/elif statement to find total distance traveled by taxi
        if xmove>=0:
            self._odometer+=xmove
        elif xmove<0:
            self._odometer-=xmove
        #adds movement of xcoord to original x_coord
        self._x_coord+=xmove
    #method to take in y direction movement and add total distance to odometer
    def move_y(self,ymove):
        if ymove>=0:
            self._odometer+=ymove
        elif ymove < 0:
            self._odometer-=ymove
        #adds movement of ycoord to original y_coord
        self._y_coord+=ymove

#cab = Taxicab(5,-8)
#cab.move_x(3)
#cab.move_y(-4)
#cab.move_x(-1)
#print(cab.get_odometer())