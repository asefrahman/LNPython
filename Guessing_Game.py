secret_numer = 5
guess_count = 0
guess = 0
guess_limit = 3
out_of_guesses = False

while guess!= secret_numer and not out_of_guesses:
    if guess_count < guess_limit:
        guess = int(input("Enter a number between 1-5: "))
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")