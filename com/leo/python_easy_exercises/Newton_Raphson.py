import math

e = 0.01
y = 24.0
guess = y / 2.0
numOfGuesses = 0
while abs(guess * guess - y) >= e:
    guess = guess - (((guess ** 2) - y) / (2 * guess))
    numOfGuesses += 1
print('Square root of', y, 'is about', guess, 'and number of guesses = ', numOfGuesses)
print('Square root using bisection is ', math.sqrt(y))
