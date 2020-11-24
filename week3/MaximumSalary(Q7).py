def isLargestOrEqualto(digit,max_digit):
    #This function checks for the best digit or number which makes the largest sequence of number(A/Q).
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))

def largestNumber(lst):
    
    #This is the list where our ans is stored is stored as list.
    answer = []
    while lst != []:
        max_digit = 0
        
        #Iterating through each digit.
        for digit in lst:

            #But the for loop will continue iterating and will give the largest possible number or digit in the given sequence.
            if isLargestOrEqualto(digit,max_digit):
                max_digit = digit
                
        #When for loop ends the we will get the first digit or number suitable to get the highest number combination.
        answer.append(max_digit)

        #At the ending of while loop we will remove that digit or number from that list.And continue.
        lst.remove(max_digit)

    return answer

#Driver Code.
n = int(input())
lst = [int(i) for i in input().split()]
print(''.join([str(i) for i in largestNumber(lst)]))

