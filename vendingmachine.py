#!/bin/python3
#This program is a vending machine that will only return coins if bills are input

def priceCheck(price, payment):
    recieved = 0
    for i in range(0,len(payment)): #Calculates total money inserted
        recieved = recieved + payment[i]
        
    price = int(price * 100)
    recieved = int(recieved*100)
    if recieved < price:
        print('Not enough money inserted')
        ChangeMaker(recieved)
    elif price == payment:
        print('Item returned with no change')
    else:
        print('item and change returned')
        ChangeMaker(recieved-price)

def ChangeMaker(recieved):    #Returns only coins from inserted money  
    returned = [0,0,0,0]
    done = False
    while True:
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
            print('Pennies: ' + str(returned[0]), ', Nickels: ' + str(returned[1]) + ', Dimes: ' + str(returned[2]) + ', Quarters: ' + str(returned[3]))
            break
    
     
##price = float(input('What is the price of the item?'))       #ORIGIANL CODE
##payment = []
##print('Enter coins and bills. Enter "Done" when finished')
##while True:
##    inserted = input()
##    if inserted != 'Done':
##        payment.append(float(inserted))
##    else:
##        break
price = 2.00            #DEBUGGING CODE
payment= [2.07]

priceCheck(price,payment)
