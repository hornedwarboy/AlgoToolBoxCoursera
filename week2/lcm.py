def lcm(a,b):
    '''
    lcm(a,b) * gcd(a,b) = a * b
    '''
    gc = gcd(a,b)
    lc = (a*b) // gc
    
    return lc

def gcd(a,b):
    ma,mi = max(a,b), min(a,b)  #Assigning max and min.
    rem = ma % mi               #Finding remainder.
    if rem == 0:                #Base Case.'''    
        return mi          
    else:
        return gcd(mi,rem)      #Recursive Part'''

#DRIVER CODE.
a,b = input().split()           #Taking two input at once.
a,b = int(a),int(b)             #Converting both the inputs into integer.
print(lcm(a,b))
        
