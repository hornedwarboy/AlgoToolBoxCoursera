def fib(n): 
    # Base cases 
    if n == 0: 
        return 0
    if n == 1 or n == 2: 
        return 1
    #Pisano Period.
    n = n % 60  

    #Formula to calculate sum of squares.
    if n & 1: 
        k = (n + 1) // 2
    else: 
        k = n // 2

    # Applying above formula[Note value 
    # n & 1 is 1 if n is odd, else 0]. 
    if n & 1: 
        f = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1)) 
    else: 
        f = ((2 * fib(k - 1) + fib(k)) * fib(k)) 
    return f 

# Function to calculate sum of 
# squares of Fibonacci numbers 
def calculateSumOfSquares(n): 

	return (fib(n) * fib(n + 1)) %10 

# Driver Code 
n = int(input())
print(calculateSumOfSquares(n)) 


