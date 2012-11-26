#Project Euler problem 1 "http://projecteuler.net/problem=1":
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Declare empty variable to hold sum:
num=0
#For all numbers below 1000, if the number is a multiple of 3 or 5, add it to others.
for i in range(1,1000):
 if i%3 == 0 or i%5 == 0:
     num = num + i
#Print answer
print "The answer is " + str(num) + "."