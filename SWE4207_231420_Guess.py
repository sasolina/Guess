import random

def quitA():
    quitA = str(input('do you want to go futher (yes) or (no)')) # this
    if quitA == 'yes' or quitA == 'Yes':
        return()
    elif quitA == 'no' or quitA == 'No':
        quit()
    else:
        print ('Invalid input, please enter yes or no ')
        quitA()

number = random.randint(1,10)

while True :
    guessnum = int(input('guess the number: '))

    if guessnum < number:
        print('Too low try again')
        quitA()
    elif guessnum > number:
        print('Too high try again')
        quitA()
    else:
        print('Well done that is correct')
        quitA()
        break

