class problema6:
   def soyPalindromo(self, palabra):  
    palabra=palabra.lower()  
    soy=True 
    n=len(palabra)  
    if n%2==0:   
        for i in range(int(n/2)):  
            if palabra[i]!=palabra[n-i-1]:  
                soy=False  
            else:  
                for i in range(int((n-1)/2)):  
                    if palabra[i]!=palabra[n-i-1]:  
                        soy=False  
    return soy 