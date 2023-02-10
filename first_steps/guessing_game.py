secret_word = "Jhon"
guess = ""
chances = 0
chances_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if chances < chances_limit:
        guess = input("Enter a word: ")
        chances+=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")