#running on CodeSkulptor
import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randint(0,100)
    return secret_number
    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global inputnumber
    inputnumber = random.randint(0,100)
    return inputnumber
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randint(0,1000)
    global inputnumber
    inputnumber = random.randint(0,1000)
    return inputnumber
    
    
def input_guess(guess):
    # main game logic goes here	
    global number
    number = int(guess)
    print "Guess is ",number
    if number < secret_number:
        print "Higher!\n"
    elif number > secret_number:
        print "Lower!\n"
    else:
        print "Correct!"
    # remove this when you add your code
    

    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("your number",input_guess,200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
