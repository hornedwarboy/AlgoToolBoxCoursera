n = int(input())
lst = []

#Taking input. 
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    lst.append((a,b))

#Sorting list according to b .Example:-
# If list is [(4, 7), (1, 3), (2, 5), (5, 6)] they will convert into  [(1, 3), (2, 5), (5, 6), (4, 7)]
lst.sort(key = lambda x: x[1])

index = 0
coordinates = []

while index < n:
    curr = lst[index]
    while index < n-1 and curr[1]>=lst[index+1][0]:
        index += 1
    #When while condition doesnt follow.
    coordinates.append(curr[1])
    index += 1

#Answers.
print(len(coordinates))
print(*coordinates)
