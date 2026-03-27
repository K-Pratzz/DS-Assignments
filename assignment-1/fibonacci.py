#fibonaci  0 1 1 2 3 
n=int(input("enter number "))

count=[0]
def fib_naive(n,count):
    count[0]+=1
    if n<=1:
        return n
    else:
        return fib_naive(n-1,count) + fib_naive(n-2,count)
for i in range(n):
    print(fib_naive(i,count),end=' ')
print("\nCount of operations :",count[0])

memo={}
def fib_memo(n,count):
    count[0]+=1
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    else:
        memo[n]=fib_memo(n-1,count)+fib_memo(n-2,count)
        return memo[n]
for i in range(n):
    print(fib_memo(i,count),end=" ")
print("\n ",count[0])

'''

Explanation of Difference:
Naive Fibonacci is slow because it recalculates the same subproblems multiple times, 
leading to exponential growth (O(2^n)). Memoization stores previous results in a table, 
ensuring each subproblem is solved only once, reducing complexity to linear (O(n)).

'''