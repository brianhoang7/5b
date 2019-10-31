class Taxicab:
    def __init__(self,x_coord,y_coord):
        self._x_coord=0
        self._y_coord=0
        self._odometer=0
    def get_x_coord(self):
        return self._x_coord
    def get_y_coord(self):
        return self._y_coord
    def get_odometer(self):
        return self._odometer
    def move_x(self,xmove):
        self._odometer+=xmove
        self._x_coord+=xmove
    def move_y(self,ymove):
        self._odometer+=ymove
        self._y_coord+=ymove
