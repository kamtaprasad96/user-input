"""Write a python script to calculate simple intrest"""

from time import time


principle=float(input("Enter the principle amount: "))
time=int(input(" Enter the time :"))
rate=float(input("Enter the rate :"))
simple_intrest=(principle*time*rate)/100
print("The simple intrest is :",simple_intrest)