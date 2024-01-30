"""
1. Write a program that asks the user to enter a string. The program should then print the
following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e
"""
# Asks the user to enter a string
enterString = input("Enter a string: ")
# a
total_n = len(enterString)
print(f'The total number of characters in the string: {total_n}')
# b
print('String repeated 10 times:', enterString*10)
# c
print('The first character of the string: ',enterString[0])
# d
print('The first three characters of the string: ',enterString[0:3])
# e
print('The last three characters of the string: ',enterString[-3:])
# f
print('The string backwards: ',enterString[::-1])
# g
if total_n >= 7:
    seventh_char = enterString[6:7]
    print('The seventh character of the string: ',seventh_char)
else: print("Does not contain 7 characters.")
# h
remove_firstlast = enterString[1:-1]
print('The removed first and last character of the string: ',remove_firstlast)
# i
print('The string in all caps: ',enterString.upper())
# j
print('String where every a replaced with an e: ',enterString.replace('a','e'))

"""
9. Ask the user for a number and then print the following, where the pattern ends at the number
that the user enters.
    1
     2
      3
       4
"""
num = input("Enter a number: ") # ask the user to enter a number
rep_1 = 0
rep_2 = 1
empty_string = 1
for i in range(len(num)): # iterates depends on the length of the string
    print(' '*empty_string,num[rep_1:rep_2])
    rep_1 += 1
    rep_2 += 1
    empty_string += 1

"""
10. Write a program that asks the user to enter a string, then prints out each letter of the string
doubled and on a separate line. For instance, if the user entered HEY, the output would be
    HH
    EE
    YY
"""
enter_string = input("Enter string: ") # ask the user to enter string
rep_1 = 0
rep_2 = 1
for i in range(len(enter_string)): # this will print each letter of the string
    print(enter_string[rep_1:rep_2]*2)
    rep_1 += 1
    rep_2 += 1

"""
13. Write a program that asks the user to enter two strings of the same length. The program
should then check to see if the strings are of the same length. If they are not, the program
should print an appropriate message and exit. If they are of the same length, the program
should alternate the characters of the two strings. For example, if the user enters abcde and
ABCDE the program should print out AaBbCcDdEe.
"""
print('Enter two strings')
first_string = input('Enter first string: ')
second_string = input('Enter second string: ')


if len(first_string) == len(second_string):
    rep_1 = 0
    rep_2 = 1
    for i in range(len(first_string)):
        print(f'{first_string[rep_1:rep_2]}{second_string[rep_1:rep_2]}', end='')
        rep_1 += 1
        rep_2 += 1
else: print("String's not on the same length.")

"""
15. When I was a kid, we used to play this game called Mad Libs. The way it worked was a friend
would ask me for some words and then insert those words into a story at specific places
and read the story. The story would often turn out to be pretty funny with the words I had
given since I had no idea what the story was about. The words were usually from a specific
category, like a place, an animal, etc.
For this problem you will write a Mad Libs program. First, you should make up a story and
leave out some words of the story. Your program should ask the user to enter some words
and tell them what types of words to enter. Then print the full story along with the inserted
words. Here is a small example, but you should use your own (longer) example:
    Enter a college class: CALCULUS
    Enter an adjective: HAPPY
    Enter an activity: PLAY BASKETBALL
    CALCULUS class was really HAPPY today. We learned how to
    PLAY BASKETBALL today in class. I can't wait for tomorrow's
    class!

I went to the (place) yesterday. I was so (emotion). I also saw (name) there, and I gave (name) my (something you own)
"""

place = input("Enter a place: ")
emotion = input("Enter an emotion: ")
name = input("Enter a name: ")
you_own = input("Enter something you own: ")

print(f'I went to the {place} yesterday. I was so {emotion}. I also saw {name} there, and I gave {name} my {you_own}.')

"""
19. Write a program that asks the user for a large integer and inserts commas into it according
to the standard American convention for commas in large numbers. For instance, if the user
enters 1000000, the output should be 1,000,000.
"""

integer = input("Enter a large number: ")
reverse = integer[::-1]
reps = 0
commafier = ""

while reps * 3 < len(integer):
    a = reps * 3
    b = a + 3
    commafier = (reverse[a:b] + ',') + commafier
    reps += 1


commafier = commafier.rstrip(',')

print(commafier)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# """
# The GCD (greatest common divisor) of two numbers is the largest number that both are divisible by. For instance, gcd(18, 42) is 6 because the largest number that both 18 and 42 are
# divisible by is 6. Write a program that asks the user for two numbers and computes their gcd.
# Shown below is a way to compute the GCD, called Euclid’s Algorithm.
# • First compute the remainder of dividing the larger number by the smaller number
# • Next, replace the larger number with the smaller number and the smaller number with
# the remainder.
# • Repeat this process until the smaller number is 0. The GCD is the last value of the larger
# number.
# """
#
# num_1 = float(input("Enter first number: "))
# num_2 = float(input("Enter second number: "))
#
# # Ensure num_1 is greater than or equal to num_2
# if num_1 < num_2:
#     num_1, num_2 = num_2, num_1
#
# while num_2 != 0:
#     remainder = num_1 % num_2
#     num_1 = num_2
#     num_2 = remainder
#
# # GCD is the last value of num_1
# gcd = num_1
#
# print("The GCD is:", gcd)

# """
# 5. Write a program that allows the user to enter any number of test scores. The user indicates
# they are done by entering in a negative number. Print how many of the scores are A’s (90 or
# above). Also print out the average.
# """
# # Initialize an empty list to store test scores
# scores = []
#
# # Prompt the user for test scores until a negative number is entered
# while True:
#     test_score = float(input("Enter a test score (enter a negative number to finish): "))
#
#     # Check if the user is done entering scores
#     if test_score < 0:
#         break
#
#     # Add the test score to the list
#     scores.append(test_score)
#
# # Count the number of A's (scores 90 or above)
# a_count = sum(score >= 90 for score in scores)
#
# # Calculate the average of all the scores
# if len(scores) > 0:
#     average = sum(scores) / len(scores)
# else:
#     average = 0
#
# # Print the results
# print("Average score:", average)

# """
# Modify the higher/lower program so that when there is only one guess left, it says 1 guess,
# not 1 guesses.
# """
#
# from random import randint
#
# secret_num = randint(1, 100)
# num_guesses = 0
# guess = 0
#
# while guess != secret_num and num_guesses < 5:
#     guess = eval(input('Enter your guess (1-100): '))
#     num_guesses += 1
#
#     if guess < secret_num:
#         remaining_guesses = 5 - num_guesses
#         if remaining_guesses > 1:
#             print('HIGHER. {} guesses left.\n'.format(remaining_guesses))
#         else:
#             print('HIGHER. 1 guess left.\n')
#
#     elif guess > secret_num:
#         remaining_guesses = 5 - num_guesses
#         if remaining_guesses > 1:
#             print('LOWER. {} guesses left.\n'.format(remaining_guesses))
#         else:
#             print('LOWER. 1 guess left.\n')
#
#     else:
#         print('You got it!')
#
# if num_guesses == 5 and guess != secret_num:
#     print('You lose. The correct number is', secret_num)

# """
# (a) Write a program that uses a while loop (not a for loop) to read through a string and print
# the characters of the string one-by-one on separate lines.
# (b) Modify the program above to print out every second character of the string.
# """
#
# string_input = input("Enter a string: ")
# index = 0
#
# while index < len(string_input):
#     print(string_input[index])
#     index += 1
#
# string_input = input("Enter a string: ")
# index = 1
#
# while index < len(string_input):
#     print(string_input[index])
#     break

"""
Write a text-based version of the game Memory. The game should generate a 5 × 5 board (see
the exercise from Chapter 8). Initially the program should display the board as a 5 × 5 grid of
asterisks. The user then enters the coordinates of a cell. The program should display the grid
with the character at those coordinates now displayed. The user then enters coordinates of
another cell. The program should now display the grid with the previous character and the
new character displayed. If the two characters match, then they should permanently replace
the asterisks in those locations. Otherwise, when the user enters the next set of coordinates,
those characters should be replaced by asterisks. The game continues this way until the player
matches everything or runs out of turns. You can decide how many turns they player gets
"""

import random

# Generate a 5x5 Memory board with pairs of symbols
symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
pairs = symbols * 2
random.shuffle(pairs)
board = [pairs[i:i+5] for i in range(0, 10, 5)]

# Initialize a 5x5 grid of asterisks to represent unrevealed cells
revealed = [["*" for _ in range(5)] for _ in range(5)]

turns = 5

try:
    while turns > 0:
        # Display the current state of the board
        for row in revealed:
            print(" ".join(row))
        print(f"Turns left: {turns}")

        # Get user input for the coordinates
        try:
            row1 = int(input("Enter the row for the first card (0-4): "))
            col1 = int(input("Enter the column for the first card (0-4): "))
            row2 = int(input("Enter the row for the second card (0-4): "))
            col2 = int(input("Enter the column for the second card (0-4): "))
        except ValueError:
            print("Invalid input. Please enter valid integers.")
            continue

        # Check if the coordinates are within the valid range
        if 0 <= row1 < 5 and 0 <= col1 < 5 and 0 <= row2 < 5 and 0 <= col2 < 5:
            # Check if the selected cards have already been revealed
            if revealed[row1][col1] != "*" or revealed[row2][col2] != "*":
                print("Those coordinates have already been revealed. Try again.")
                continue

            # Check if the selected cards match
            if board[row1][col1] == board[row2][col2]:
                print("Match found!")
                revealed[row1][col1] = board[row1][col1]
                revealed[row2][col2] = board[row2][col2]
            else:
                print("No match. Try again.")
                revealed[row1][col1] = "*"
                revealed[row2][col2] = "*"
                turns -= 1

            # Check if all pairs have been matched
            if all(cell != "*" for row in revealed for cell in row):
                print("Congratulations! You've matched all pairs.")
                break

        else:
            print("Invalid coordinates. Please enter values between 0 and 4.")

    print("Game over!")
except Exception:
    print("Error!")


