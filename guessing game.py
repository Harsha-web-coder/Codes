
##guessing game
import random
print('To stop anytime, enter: q')
score = 0
while True:
    num = random.randint(0,10)
    guess = input("Guess a number between 0 to 10: ")
    if guess == 'q':
        print('Game Over.')
        break
    guess_num = int(guess)
    if guess_num is num:
        print('CONGRATS, you guessed it correctly')
        score += 10
        print('Your new score:', score)
    else:
        print('Your guess did not match')
        print('The number was:', num)
