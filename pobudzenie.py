class Pobudzenie:
    def __init__(self, length, type, amplitude, width):
        self.length = length
        self.type = type
        self.values = []
        self.amplitude = amplitude
        self.width = width
        self.y = self.create_list_value()

    def create_list_value(self):

        if(self.type == "square"):
            for i in range (0,self.width):
                self.values.append(self.amplitude)
            for i in range (self.width, self.length):
                self.values.append(0)

        if(self.type == "triangle"):
            self.values.append(0)
            loop_num = int(self.length / self.width) + 1
            for i in range (0, loop_num):
                if(self.width % 2 == 0):
                    half = int((self.width)/2)
                else:
                    half = int((self.width - 1)/2)
                for i in range(1, half+1):
                    self.values.append(self.amplitude * i / (half + 1))
                self.values.append(self.amplitude)
                for i in range(-half, 0):
                    self.values.append(self.amplitude * (-i) / (half + 1))
                self.values.append(0)
            reszta = len(self.values) - self.length
            for i in range(0, reszta):
                self.values.pop()

        return self.values

    def value_return(self):
        return self.y