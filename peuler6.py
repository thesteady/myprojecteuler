#Project Euler, Problem 6 "http://projecteuler.net/problem=6":
#The sum of the squares of the first ten natural numbers is  12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Declare empty variables so I know what variables I have:
x=0
y=0
ans=0
#for all integers in range, add them appropriately to the sum of squares(x) or sum (y)
for i in range(1,101):
    #add the squared value of the integer to the previous ones
    x=x + i**2
    #add the value to the previous values
    y=y+i
#Find the answer to the question:
ans= (y**2)-x
print "The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is " + str(ans) + "."