import random

def guess(x):
   random_number = random.randint(1, x)
   guess = 0
   while guess != random_number:
      guess = int(input(f'guess a num between 1 and {x}: '))
      if guess < random_number:
         print('guess is too low')
      elif guess > random_number:
         print('guess is too high')
      else:
         print(f'yay! you win! the random number was {random_number}')

def computer_guess(x):
   low = 1
   high = x
   feedback = ''
   while feedback != 'c':
      if low != high:
         guess = random.randint(low, high)
      else:
         guess = low

      feedback = input(f'is {guess} too high (H), too low (L), or correct (c)?').lower()

      if feedback == 'h':
         high = guess - 1
      elif feedback == 'l':
         low = guess + 1
      else:
         print(f'the computer guessed the number {guess} correctly')


computer_guess(1000)