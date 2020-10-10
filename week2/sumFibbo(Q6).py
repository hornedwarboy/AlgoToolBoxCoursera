def pp():                           #Function to calculate PISANO PERIOD of 10.
    p1, p2 = 0, 1                   #As we have to find the last digit of sum of series. 
    for i in range(100):            
        p1, p2 = p2, (p1+p2) % 10

        if p1 == 0 and p2 == 1:
            return i+1

def sumF(n):                                        #Function to calculate sum of series.
    p = pp()                            
    n = n % p                                       #This gives the no. of times the for loop will run.
    prev, curr = 0, 1
    summ = 1
    #WORKING OF THIS FUNCTION:-
        #We find the period in which mod 10 of fibonacci series work
        #We have to find the last digit of the sum of series.
        #So if we just find for a particular period the rest will repeat itself.
        #Therefore we use Pisano Period

    
    if n == 0 or n == 1:                            #Base CASE.
        return n
    
    else:
        for i in range(n-1):                        
            prev, curr = curr, (curr+prev)%10
            summ = summ + curr                      #Calculating Sum.

        return summ%10

#Driver Code.
n = int(input())
print(sumF(n))
