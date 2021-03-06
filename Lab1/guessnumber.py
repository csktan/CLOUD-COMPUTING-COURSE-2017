
#program to guess the number
#   @csktan

import random
import math

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
# initialize global variables used in your code
num_range = 20
secret_num = 0
guesses_left = 0


# helper function to start and restart the game
def new_game():  
    global num_range
    global secret_num
    global guesses_left
    
    secret_num = random.randrange(0, num_range)
    
    if num_range == 20 :    
        guesses_left = 3
       

    print ("New game. The range is from 0 to") , num_range, (". Good luck!")
    print ("Number of remaining guesses is ") , guesses_left, ("\n")
    pass

# define event handlers for control panel
def range20():
    global num_range
    num_range = 20 # button that changes range to range [0,20) and restarts
    new_game() 
    pass

   
def input_guess(guess):    
    # main game logic goes here 
    global guesses_left
    global secret_num 
    
    won = False
    
    print ("You guessed: "),guess
    guesses_left = guesses_left - 1
    print ("Number of remaining guesses is "), guesses_left
    
    if int(guess) == secret_num:       
        won = True
    elif int(guess) > secret_num:
        result = "Lower!"
    else:
        result = "Higher!"                
        
        
    if won:
        print ("That is correct! Congratulations!\n")
        new_game()
        return
        print ("Game over. You didn't guess the number in time!")   
        new_game()
        return
    else:
        print (result)
        pass
            
    
# create frame
f = simplegui.create_frame("Game: Guess the number!", 200, 250)
f.set_canvas_background('Green')

# register event handlers for control elements
f.add_button("Range is [0, 20)", range20, 20)
f.add_input("Enter your guess", input_guess, 20)

# call new_game and start frame
new_game()
f.start()
