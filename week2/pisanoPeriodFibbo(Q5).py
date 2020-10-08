def pissanoPeriod(m):
    #If F(n) is nth fibbo number,
    #And we need to calculate F(n) % m,
    #It is periodic and we can calculte the period using the function pissanoPeriod.
    #This period always starts with 0,1.
    previous,current = 0,1
    for i in range(0,m*m):
        previous,current = current, (previous+current)%m

        if previous == 0 and current == 1:
            return i+1

def fibA(n,m):
    pp = pissanoPeriod(m)
    n = n % pp                              #This gives the loop interval.
    prev, curr =0, 1
    if n == (0 or 1):                       #BAse Case.
        return n
    else:
        for i in range(n-1):
            prev, curr = curr, prev+curr    #Calculating(F(n) % m)

    return (curr % m)

#DRIVER CODE.
n, m = input().split()
n, m = int(n), int(m)
print(fibA(n,m))
