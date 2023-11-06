import random
print("Welcome to the number guessing game! \nI am thinking of a number between 1 to 100")
difficulty =input("Choose a difficulty. Type 'easy' or 'hard': ")
tries = 0
if difficulty == "easy":
  print(1)
  tries += 10
elif difficulty == "hard":
  tries += 5
number = random.randint(1,101)
while tries != 0:
  guess = int(input(f"You have {tries} attempts remaining to guess the number \nMake a guess: "))
  if guess != number:
    if guess >= number:
      print("Too High")
    elif guess <= number:
      print("Too Low")
    tries -= 1
  else:
    print(f"You got the number {guess}={number}")
    tries = 0 