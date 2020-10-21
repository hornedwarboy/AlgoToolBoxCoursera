def moneyChange(tm):
    #Initial number of coins.
    c1, c5, c10 = 0, 0, 0
    
    #Starting the loop and this loop will break if tm(total_money == 0).
    while tm > 0:
        #Using greedy technique(most greedy solution first.)
        if tm >= 10:
            tm = tm - 10
            #c10(coin of 10)
            c10 = c10 + 1
            if tm == 0:
                return c1, c5, c10
            
            
        elif tm < 10 and tm >= 5:
            tm = tm - 5
            #c5(coin of 5)
            c5 = c5 + 1
            if tm == 0:
                return c1, c5, c10
            

        elif tm > 0 and tm < 5: 
            tm = tm - 1
            #c1(Coin of 1)
            c1 = c1 + 1
            if tm == 0:
                return c1, c5, c10


    return c1, c5, c10

    
            


#Driver code.
n = int(input())
a, b, c = moneyChange(n)
print(a+b+c)#Solution is to print minimum numbers of coin needed.
