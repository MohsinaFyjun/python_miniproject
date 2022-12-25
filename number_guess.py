# ###------- GUESS A NUMBER PYTHON PROJECT------- ###
# # random number import
# # take any number betwn 1 to 10
# # run a loop until right guess
# # guess if it is low or high?

# import random                                             
# n = random.randrange(1,10)
# print()
# guess = int(input("Enter any number: "))                  

# while n!= guess:                                           
#     if guess < n:                                          
#         print("Hey, i think your guess is LOW")            
#         print()
#         guess = int(input("Enter number again: "))
#     elif guess > n:                                        
#         print("Hey, i think your guess is HIGH")
#         print()
#         guess = int(input("Enter number again: "))
#     else:
#       break                                                

# print("yee , you guessed it right!!")

# # simple code but will be add more range using function and method
def play_game():
   secret_number = random.randint(1, 1000)
   guess = int(input("Guess a number between 1 and 1000:"))
   guess_count = 1
   while secret_number != guess:
      if guess > secret_number:
         guess = int(input("Guess a lower number: "))
      elif guess < secret_number:
         guess = int(input("Guess a higher number: "))
      guess_count += 1
print(f"Yay! You won in turns!")


import random

randomNumber = random.randrange(1, 1000)

def main():
    print ()
    number = input("I have a number between 1 and 1000. Can you guess my number? Please type your first guess: ")
    guess(number)

def guess(number1):
    correct = False
    while not correct:
        if number1 > randomNumber:
            print ("Too high. Try again.")
            print ()
        elif number1 < randomNumber:
            print ("Too low. Try again.")
            print ()
        elif number1 == randomNumber:
           break
        number1 = input ("What number do you guess? ")
    if number1 == randomNumber:
       playAagain = raw_input ("Excellent! You guessed the number! Would you like to play again (y or n)? ")
       if playAagain == "y":
            main()