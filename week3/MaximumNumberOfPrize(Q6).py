#Taking input.
n = int(input())

#Base Case. 
if n == 1:
    print(1)
    print(1)
    quit()
W = n
prizes = []

#Collecting outputs.
for i in range(1, n):
    if W>2*i:
        prizes.append(i)
        W -= i
    else:
        prizes.append(W)
        break

#Printing Outputs.
print(len(prizes))
print(' '.join([str(i) for i in prizes]))
