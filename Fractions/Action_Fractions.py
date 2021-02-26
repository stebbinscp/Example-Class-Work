# fraction program 

from math import gcd
from Fraction_class import Fraction
import random

def random_fraction():
    """Randomly generate a function"""
    numerator = random.randint(1,9)
    denominator = random.randint(1,9)
    frac = Fraction(numerator,denominator)
    # print(frac)
    return frac

def random_operation():
    """Randomly generate an operation"""
    operation = random.choice(["add","subtract","multiply","divide"])
    return operation

def fraction_program(operation, frac, frac_2):
    """Run the fraction question"""
    if operation == "add":
        question = f"What is {frac} + {frac_2}?"
        answer = frac+frac_2
    elif operation == "subtract":
        question = f"What is {frac} - {frac_2}?"
        answer = frac-frac_2
    elif operation == "multiply":
        question = f"What is {frac} * {frac_2}?"
        answer = frac*frac_2
    else:
        question = f"What is {frac} / {frac_2}?"
        answer = frac/frac_2
    print(question)
    return answer

def main():
    """Run the fraction question generator until the user decides to stop"""
    print("Welcome to Action Fractions!!")
    count = 0
    total = 0
    while True:
        f1 = random_fraction()
        f2 = random_fraction()
        operation = random_operation()
        # print(operation)
        answer = fraction_program(operation,f1,f2)
        answer = answer.__str__()
        # print(answer)
        user_input = input("Input your answer: ")
        if user_input == answer:
            count += 1
            total += 1
            print("That was right :) ")
        else:
            total += 1
            print(f"That was wrong :(, the answer was {answer} ")
        repeat = input("Would you like to try again?  (y/n)")
        if repeat == "y":
            continue
        elif repeat == "n":
            break
        else:
            print("Sorry, we didn't recognize that input!", end="")
            print("I'll end the program for you!")
    print(f"You got {count}/{total} correct!")
        

if __name__ == "__main__":
    main()

# write a program to practice fraction operations

# randomly selected operation

# randomly generated fractions

# keep track of the completed and attempted problems

# offer them to keep playing