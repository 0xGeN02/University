#Generate a store data to generate all cards one by one
#redirect to Lab03_03.py
import random
random.seed(10)

x = 0
while(x<48):

    x = x+1
    #First we generate an algorithmm that generates a card randomly
    Generate_Number = random.randint(1,48)

    #Now we add the variable Sotore card which will help us with not repeating a card
    Card_Shared = range(1, 49)
    Stored_Number = Card_Shared - Generate_Number

    #Algorithm to name the card which variation depends on the randomizer done before
    if Generate_Number == 1 or 13 or 25 or 37:
        print("As ",end=" ")
    elif Generate_Number == 10 or 22 or 34 or 46:
        print("Sota ",end=" ")
    elif Generate_Number == 11 or 23 or 35 or 47:
        print("Caballo ",end=" ")
    elif Generate_Number == 12 or 24 or 36 or 48:
        print("Rey ",end=" ")
    else:
        print(Generate_Number)

    if Generate_Number < 13:
        print(" de Oros")
    elif Generate_Number < 25:
        print("de Espadas")
    elif Generate_Number < 37:
        print("de Bastos")
    else:
        print("de Copas")

