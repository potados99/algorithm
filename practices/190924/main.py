#!/usr/bin/python

from algorithm import isPerfect
from algorithm import isPrime
from algorithm import divisorSum
from algorithm import printNum
from algorithm import cocktailShaker
from algorithm import exchangeSortReversed

from copy import deepcopy as cp

l = [9,3,7,45,5,11,8,423,25,63]

print("IsPerfect(6): " + str(isPerfect(6)))
print("IsPerfect(28): " + str(isPerfect(28)))
print("IsPerfect(12): " + str(isPerfect(12)))
print("IsPerfect(10): " + str(isPerfect(10)))
print
print("IsPrime(2): " + str(isPrime(2)))
print("IsPrime(17): " + str(isPrime(17)))
print("IsPrime(36): " + str(isPrime(36)))
print
print("printNum(17):")
printNum(17)
print
print("cocktailShaker(l):")
cocktailShaker(cp(l), True)
print
print("exchangeSortReversed(l):")
exchangeSortReversed(cp(l), True)
