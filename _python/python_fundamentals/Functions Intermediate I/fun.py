import random
import math
countt=0
def randInt(min=0  , max=100 ):
    global countt
    num=random.random() * (max-min) + min
    num=round(num)
    if(min>max ):
        countt=countt+1 
        
    return num

print(randInt()) 		# should print a random integer between 0 to 100
print(randInt(max=50)) 	# should print a random integer between 0 to 50
print(randInt(min=50)) 	# should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500 
print(randInt(min=500, max=50))
print(randInt(min=500, max=-1))  
print(countt)
