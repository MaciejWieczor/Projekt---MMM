class Pobudzenie:
    def __init__(self, length, type, amplitude, square_width):
        self.length = length
        self.type = type
        self.values = []
        self.amplitude = amplitude
        self.square_width = square_width
        self.y = self.create_list_value()

    def create_list_value(self):
        if(self.type == "square"):
            for i in range (0,self.square_width):
                self.values.append(self.amplitude)
            for i in range (self.square_width, self.length):
                self.values.append(0)
        return self.values

    def value_return(self):
        return self.y