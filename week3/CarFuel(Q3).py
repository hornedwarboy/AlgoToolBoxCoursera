def CFuel(total_dist, milage, no_of_Gstops, Gstops):
    numRefill, currRefill = 0, 0
    while currRefill <= no_of_Gstops:
        #Initially where we start we have lastRefill -> currRefill.
        lastRefill = currRefill
        #Greedy approach we want as less no of refills as possible.
        while currRefill <= no_of_Gstops and (Gstops[currRefill + 1] - Gstops[lastRefill]) <= milage:
            currRefill = currRefill + 1
            
        #Impossible to reach destination if this happens.
        if currRefill == lastRefill:
                return -1
            
        if currRefill <= no_of_Gstops:
                numRefill = numRefill + 1

    return numRefill
            
            


#Driver Code.
total_dist = int(input())
milage = int(input())
no_of_Gstops = int(input())
l = input().split()
Gstops = [0]
for i in range(no_of_Gstops):
    l[i] = int(l[i])
    Gstops.append(l[i])
    
Gstops.append(total_dist)
print(CFuel(total_dist, milage, no_of_Gstops, Gstops))

