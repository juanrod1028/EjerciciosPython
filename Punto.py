class punto:
    
    def __init__(self,x,y):
        self.x=x    
        self.y=y


    def hallarDistancia(self, otro):
        distancia= ((self.x-otro.x)**2 + (self.y-otro.y)**2)**(1/2) 
        return distancia