#running on CodeSkulptor
import simplegui
import random
import math
times = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print"Let's start the game!\n"

      
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randint(0,100)
    return secret_number

    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randint(0,1000)

    
    
def input_guess(guess):
    # main game logic goes here	
    global number
    number = int(guess)
    print "Guess is ",number,".",
    global times
    times = times + 1
    print"You have played %d times."%times
    if number < secret_number:
        print "Higher!\n"
    elif number > secret_number:
        print "Lower!\n"
    else:
        print "Correct!\n"
    
    

    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("your number",input_guess,200)

# call new_game 
new_game()


# always remember to check your complet
