def fractionalKnapsack(lst,tw,n):
    #v = value, w = weight of the element, r = v/w.
    #tw = totalWeight that our bag can carry.
    #n = no. of elements.


    #Sorting the list of tuples taking 3rd element of tuple as the sorting parameter.
    #In this case tuple is of the form (v,w,r) .
    #Using lambda to sort.
    res = sorted(lst, key = lambda x: x[2],reverse=True)

    #Initially bag has 0 value.We fill the bag and value increases and left space decreases.
    tv = 0
    #Looping n times.
    for i in range(n):
        #Case where fraction of object can be added in bag( bag is partially filled).
        #Ex. bag has 10 kg left but the objects weight is 20kg, so 10kg of that object can be added.
        if tw > 0 and res[i][1] > tw:
            tv = tv+((res[i][0] / res[i][1]) * tw)
            tw = tw - res[i][1]

        if tw > 0:        
            tw = tw - res[i][1]
            tv = tv + res[i][0]
            
            #If bag is filled completly.
            if tw == 0:
                return tv

            

    return tv



        
#Drver Code.
n, tw = input().split()
n, tw= int(n), int(tw)
lst = []

#Creating a list of tuples.
for i in range(n):
    v, w = input().split()
    v, w = int(v), int(w)
    r = v/w
    lst.append((v,w,r))
#Calling function.
print(fractionalKnapsack(lst,tw,n))
