
import math

def pythagorean_theorem(ap,bp):
    
    #a^2 + b^2 = c^2
    
    #set variables
    
    a = float(ap)
    b = float(bp)
    c = a*a + b*b
    c = math.sqrt(c)
    print("the third side is", c)


ax=(input("enter the first side of the triangle"))
bx=(input("enter the second side of the triangle"))

pythagorean_theorem(ax,bx)

    
    
