import math

class Odpowiedz_impulsowa:
    def __init__(self, length, step, a1, a0, b2, b1, b0, T):
        self.length = length
        self.step = step
        self.a1 = a1
        self.a0 = a0
        self.b2 = b2
        self.b1 = b1
        self.b0 = b0
        self.T = T
        self.x = self.declare_index()
        self.y = self.calculate_values()

    def declare_index(self):
        indexes = []
        if(self.T < 0):                                  ## jeżeli T < 0, to przesunięcie jest liczone poprzez przesunięcie wartości czasu dla indeksu w lewo o T
            for n in range(0, self.length):
                indexes.append(n*self.step - self.T)
            return indexes

        for n in range(0, self.length):
            indexes.append(n*self.step)
        return indexes

    def calculate_values(self):

        values = []

        if(self.b2 == 0):       ##b2 musi być różne od 0, inaczej będzie dzielenie przez 0
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

        elif(tmp < 0):

            tmp = -tmp
            tmp = math.sqrt(tmp)

            for t in range(0,self.length):
                values.append(math.exp(-1*self.b1*self.x[t]/(2*self.b2)) * 
                              ( ( 2*self.a0*self.b2 - self.a1*self.b1 ) * math.sinh( tmp*self.x[t]/( 2*self.b2 ) )/tmp 
                               + self.a1*math.cosh( tmp*self.x[t]/( 2*self.b2 ) )) / self.b2)

        elif(tmp == 0):

            for t in range(0,self.length):
                values.append(math.exp(-1*self.b1*self.x[t]/(2*self.b2)) * ((( 2*self.a0*self.b2 - self.a1*self.b1 ) * self.x[t] / (2*self.b2*self.b2)) + self.a1/self.b2))
        

        ## tutaj jest przesunięcie o T, jeżeli T jest dodatnie
        if(self.T > 0):
            n = 0
            while(self.T > n*self.step):
                values.insert(0,0)
                values.pop()
                n += 1

        return values


    def index_return(self):
        return self.x
    
    def value_return(self):
        return self.y


x = Odpowiedz_impulsowa(10, 0.1, 1, 1, 1, 1, 1, -0.1)

print(x.index_return())
print(x.value_return())