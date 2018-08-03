"""
Guess your number game
"""
print("Guess your number between 0 to 100:")

LOW_GUESS = 0
HIGH_GUESS = 100

while True:
    GUESS_APPROX = (LOW_GUESS + HIGH_GUESS)//2
    USER_RESPONSE = input("if your guess is "+str(GUESS_APPROX)+"\
     hit 'y' else hit some other key:\n")

    if USER_RESPONSE == 'y':
        break

    USER_RESPONSE = input("If your guess is less than "+str(GUESS_APPROX)+"\
        , type 'low', else type 'high':\n")

    if USER_RESPONSE == "low":
        HIGH_GUESS = GUESS_APPROX
    elif USER_RESPONSE == "high":
        LOW_GUESS = GUESS_APPROX
