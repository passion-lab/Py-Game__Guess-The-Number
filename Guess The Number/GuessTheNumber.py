# Exercise 3 - Guess the Number
# Objective - Limited no. of guesses 9, print no. of guesses left, no. of guesses he took to finish, game over


title = "Exercise 3 - Guess the Number"
subtitle = "[Note: Guess the number in a limited attempts and see how you predict]"
underline = int(len(subtitle)) * "-"
print("\n{}\n{}\n{}\n".format(title, underline, subtitle))

GuessNum = 62
AttemptLimit = 9
Attempt = 0

while 0 < AttemptLimit:
    Guessed = int(input("Try to guess a number (only integer): "))
    Attempt += 1
    if Guessed == GuessNum:
        print("WELL DONE, You've guessed just the right number in", Attempt, "attempts!")
        break
    else:
        AttemptLimit -= 1
        print("\nOOPS, You can't guess the right this time!")
        if Guessed < GuessNum:
            print("Hint: You should guess a higher number instead.")
        else:
            print("Hint: You should guess a lower number instead.")
        print("No of attempt you've left:", AttemptLimit, "\n\n")
        continue
