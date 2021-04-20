import math

class Odpowiedz_impulsowa:
    def __init__(self, length, step, a1, a0, b2, b1, b0):
        self.length = length
        self.step = step
        self.a1 = a1
        self.a0 = a0
        self.b2 = b2
        self.b1 = b1
        self.b0 = b0
        self.x = self.declare_index()
        self.y = self.calculate_values()

    def declare_index(self):
        indexes = []
        for n in range(0, self.length):
            indexes.append(n*self.step)
        return indexes

    def calculate_values(self):

        values = []

        if(self.b2 == 0):
            for i in self.x:
                values.append(0)
            return values

        tmp = 4*self.b0*self.b2-self.b1*self.b1
    
        if(tmp > 0):

            tmp = math.sqrt(tmp)

            for t in range(0,self.length):
                values.append(math.exp(-1*self.b1*self.x[t]/(2*self.b2)) * 
                              ( ( 2*self.a0*self.b2 - self.a1*self.b1 ) * math.sin( tmp*self.x[t]/( 2*self.b2 ) )/tmp
                               + self.a1*math.cos( tmp*self.x[t]/( 2*self.b2 ) )) / self.b2)

            return values

        elif(tmp < 0):

            tmp = -tmp
            tmp = math.sqrt(tmp)

            for t in range(0,self.length):
                values.append(math.exp(-1*self.b1*self.x[t]/(2*self.b2)) * 
                              ( ( 2*self.a0*self.b2 - self.a1*self.b1 ) * math.sinh( tmp*self.x[t]/( 2*self.b2 ) )/tmp 
                               + self.a1*math.cosh( tmp*self.x[t]/( 2*self.b2 ) )) / self.b2)

            return values

        elif(tmp == 0):

            for t in range(0,self.length):
                values.append(math.exp(-1*self.b1*self.x[t]/(2*self.b2)) * ((( 2*self.a0*self.b2 - self.a1*self.b1 ) * self.x[t] / (2*self.b2*self.b2)) + self.a1/self.b2))
                
            return values


    def index_return(self):
        return self.x
    
    def value_return(self):
        return self.y