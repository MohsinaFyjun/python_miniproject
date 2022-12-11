###------- GUESS A NUMBER PYTHON PROJECT------- ###
# random number import
# take any number betwn 1 to 10
# run a loop until right guess
# guess if it is low or high?

import random                                              
n = random.randrange(1,10)
print()
guess = int(input("Enter any number: "))                  

while n!= guess:                                           
    if guess < n:                                          
        print("Hey, i think your guess is LOW")            
        print()
        guess = int(input("Enter number again: "))
    elif guess > n:                                        
        print("Hey, i think your guess is HIGH")
        print()
        guess = int(input("Enter number again: "))
    else:
      break                                                

print("yee , you guessed it right!!")

# simple code but will be add more range using function and method