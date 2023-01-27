#created by CodingwithJan

#rock paper scissors game
import random

#username
print('pick a username')
username = input('username: ')
print('hello ', username, ' and welcome to rock paper scissors game')

def game():

    #potential choices
    options = ['rock', 'paper', 'scissors']

    #user move
    userMove = input('rock, paper, scissors: ')

    #computer move
    computerMove = random.choice(options)

    #winning conditions
    if userMove == computerMove:
        print('tie')

    elif userMove == 'rock' and computerMove == 'scissors':
        print('you win')


    elif userMove == 'rock' and computerMove == 'paper':
        print('you lose')


    elif userMove == 'paper' and computerMove == 'rock':
        print('you win')


    elif userMove == 'paper' and computerMove == 'scissors':
        print('you lose')


    elif userMove == 'scissors' and computerMove == 'paper':
        print('you win')


    elif userMove == 'scissors' and computerMove == 'rock':
        print('you lose')


    else:
        print('invalid input')

    #new game
    newGame = input('play again (y/n): ')
    if newGame == 'y':
        game()
    else:
        print('goodbye')
        exit()

game()