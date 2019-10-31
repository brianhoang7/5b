class Taxicab:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.odometer = odometer
    def get_x_coord(self):
        return self.x_coord
    def get_y_coord(self):
        return self.y_coord
    def get_odometer(self):
        return self.y_coord
    def move_x(self,xmove):
        self.odometer+=xmove
        self.x_coord+=xmove
    def move_y(self,ymove):
        self.odometer+=ymove
        self.y_coord+=ymove
