# 5) Calculate the sum of consecutive integers from 1 to n
def sum_of_consecutive_integers(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum

# 6) Print all prime numbers below n
def print_prime_numbers(n):
  prime_numbers = []
  for num in range(2, n):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        is_prime = False
        break
    if is_prime:
      prime_numbers.append(num)
  print(prime_numbers)

# 7) Print the first n triangular numbers
def print_triangular_numbers(n):
  triangular_numbers = []
  for i in range(n):
    triangular_numbers.append(int(i * (i + 1) / 2))
  print(triangular_numbers)

# 8) Print the first n Lucas numbers
def print_lucas_numbers(n):
  lucas_numbers = [2, 1]
  for i in range(2, n):
    lucas_numbers.append(lucas_numbers[i-1] + lucas_numbers[i-2])
  print(lucas_numbers)

# 9) Implement a password prompt
def password_prompt():
  correct_password = "your_password"
  while True:
    password = input("Enter password: ")
    if password == correct_password:
      print("Correct password!")
      break
    else:
      print("Incorrect password. Please try again.")

# 10) Guess a random number game
import random

def guess_random_number():
  random_number = random.randint(1, 100)
  attempts = 5

  while attempts > 0:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == random_number:
      print("Congratulations! You guessed the number in", 6 - attempts, "attempts.")
      break
    elif guess < random_number:
      print("Your guess is too low.")
    else:
      print("Your guess is too high.")
    attempts -= 1

  if attempts == 0:
    print("Sorry, you ran out of attempts. The correct number was", random_number)

# Example usage
n = int(input("Enter n: "))
print("Sum of 1 to n:", sum_of_consecutive_integers(n))
print_prime_numbers(n)
print_triangular_numbers(n)
print_lucas_numbers(n)
password_prompt()
guess_random_number()