#No. 1
a = False
b = True
c = False

print(b and c)
print(b or c)
print (not a and b)
print ((a and b) or not c)
print (not b and not (a or c))

#No. 2
print('Hello!')
something = input("Enter Something : ")
print('You entered:', something )

#No. 3
print('Hello!')
something = input("Enter Something: ")
if something == 'hello':
  print('Hello For You Too!')
elif something == 'hi':
  print('Hi There!')
else:
  print('I Dont Know What,', something, 'Means')

#No. 4

repeats = 'Hai Hallo' * 11
print(repeats)

import random

user_action1 = input("Player 1 (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
user_action2 = input("Player 2 (rock, paper, scissors): ")
print(f"\nPlayer 1 chose {user_action1}, Player 2 chose {user_action2}.\n")

if user_action1 == user_action2:
    print(f"Both players selected {user_action1}. It's a tie!")
elif user_action1 == "rock":
    if user_action2 == "scissors":
        print("Rock smashes scissors! Player 1 win!")
    else:
        print("Paper covers rock! Player 2 win.")
elif user_action1 == "paper":
    if user_action2 == "rock":
        print("Paper covers rock! Player 1 win!")
    else:
        print("Scissors cuts paper! Player 2 win.")
elif user_action1 == "scissors":
    if user_action2 == "paper":
        print("Scissors cuts paper! Player 1 win!")
    else:
        print("Rock smashes scissors! Player 2 win.")

#No 6.
x = input("Input something : ")
while(x != "berhenti"):
    print("Program execute!")
    x = input("Input something : ")
print("Program stopped working !!!")
