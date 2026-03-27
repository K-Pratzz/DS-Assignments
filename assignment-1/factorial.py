#Aim: To implement factorial recursively and trace stack growth.

n=int(input("enter number "))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))

'''
Call Stack Trace for factorial(4):
​factorial(4) calls factorial(3)
​factorial(3) calls factorial(2)
​factorial(2) calls factorial(1)
​factorial(1) returns 1
​factorial(2) returns 2 * 1 = 2
​factorial(3) returns 3 * 2 = 6
​factorial(4) returns 4 * 6 = 24
​Complexity:
​Time: O(n) because there are n recursive calls.
​Space: O(n) due to the depth of the recursion stack.

'''