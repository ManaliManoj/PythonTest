secret = 9
limit = 3
count = 0
while count < limit:
    guess = int(input('Guess: '))
    count += 1
    if guess == secret:
        print('You won')
        break
else:
    print('Sorry, you failed')
