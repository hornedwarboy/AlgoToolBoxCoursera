def MDP(n,p,c):
    #Using Greedy Technique.
    #We sort both lists in ascending order
    p.sort()
    c.sort()
    ans = list()
    for i in range(n):
        #To find the most greedy solution we multiply lowest no in list1 with lowest no in list2.
        ans.append(p[i]*c[i])
    #We use sum function to find the sum directly.
    return sum(ans)
    


#Driver Code.
n = int(input())
prices = [int(prices) for prices in input().split()[:n]]
clicks = [int(clicks) for clicks in input().split()[:n]]
print(MDP(n,prices,clicks))
