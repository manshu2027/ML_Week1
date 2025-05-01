//guessing game

import random
ans = random.randint(1,100)
attempts = 4

print("Guess the no.(between 1 to 100). You have 4 life ")

for i in range(attempts):
 try:
     guess = int(input(f"Attempts {i+1}: "))
     if guess == ans:
        print("you win.")
         break
     elif guess<ans:
       print("too low.")
     else:
       print("too high. ")
     except valueError:
       print("invalid input. Try again.")
     continue
else:
  print(f"correct nmber was {ans}.")