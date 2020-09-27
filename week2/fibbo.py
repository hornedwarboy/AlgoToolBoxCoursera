def fibbo(n):
    
    if n <=1:                   #If 'n' is 0 or 1 it will return the no. itself.
        return n
    else:                       #For 'n' other than 0 or 1.
        fi,se = 0,1             #Let us take two variables and assign them with values 0 and 1 "because f(0) = 0 and f(1) = 1."
        for i in range(1,n):    #To find the nth fibbonacci number if we have assigned 2 nos. previously we just need to loop n-2 times.
            temp = fi+se        #We use temp as the nth fibbonacci number.
            fi,se = se,temp     #We update the two initially assigned variables for each loop.SO that temp can be updated.

        return temp             #We return the nth fibbonacci number.

#Driver code.
n = int(input())
print(fibbo(n))
