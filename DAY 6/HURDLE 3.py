def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()

def one_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        one_jump()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
