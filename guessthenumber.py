#running on CodeSkulptor
import simplegui
import random
import math

number_range = 100

secret_number = 0
# helper function to start and restart the game
def new_game():
    global number_range
    
    global times_left
    if number_range == 100:
        times_left = 7
    elif number_range == 1000:
        times_left = 10
        
    global secret_number
    
    secret_number = random.randint(0,number_range)
    return secret_number

    print"Let's start the game!\n"

        
    print"%d times guesses left"%times_left

      
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number_range
    number_range = 100
    new_game()

        
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number_range
    number_range = 1000
    new_game()

    
    
def input_guess(guess):
    # main game logic goes here	
    global times_left
    global secret_number
    
    print "Your number is %d."%int(guess)
    times_left = times_left - 1
    print "You have %d times left."%times_left
    
    if secret_number == int(guess):
        print"Coreect!\n"
        new_game()
    elif secret_number > int(guess):
        print"Higher!\n"
    else:
        print"Lower!\n"
    
    if times_left == 0:
        print"Times up!Let's do it again!\n"
        new_game()
    
    
    

    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("your number",input_guess,200)

# call new_game 
new_game()
frame.start()

