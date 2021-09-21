#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'ChangeMaker' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. FLOAT price
#  2. FLOAT_ARRAY payment
#

def ChangeMaker(price, payment):
    # Write your code here
    recieved = 0
    for i in range(0,len(payment)):
        recieved = recieved + payment[i]
        
    price = int(price * 100)
    recieved = recieved*100
    returned = [0,0,0,0]
    done = False
    
    if recieved < price: #not enough money inserted
        while done == False:
            if recieved>= 25:
                returned[3] = returned[3] + 1
                recieved = recieved - 25
                continue
            elif recieved >= 10:
                returned[2] = returned[2] + 1
                recieved = recieved - 10
                continue
            elif recieved >= 5:
                returned[1] = returned[1] + 1
                recieved = recieved - 5
                continue
            elif recieved >= 1:
                returned[0] = returned[0] + 1
                recieved = recieved - 1
                continue
            else:
                return(returned)
                done = True
    
    elif recieved == price: #payment is the exact price
        return([0,0,0,0])
    else:                       #payment is more than the price
        recieved = recieved - price
        while done == False:
            if recieved>= 25:
                returned[3] = returned[3] + 1
                recieved = recieved - 25
                continue
            elif recieved >= 10:
                returned[2] = returned[2] + 1
                recieved = recieved - 10
                continue
            elif recieved >= 5:
                returned[1] = returned[1] + 1
                recieved = recieved - 5
                continue
            elif recieved >= 1:
                returned[0] = returned[0] + 1
                recieved = recieved - 1
                continue
            else:
                return(returned)
                done = True
        
                
price = 1.27
payment = [1.00,.25,.10]
print(ChangeMaker(price,payment))
