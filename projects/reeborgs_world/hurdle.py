def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    # Keep going up until the hurdle is jumped over
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    # Keep going down until the ground is found
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    # Keep walking until a hurdle is encountered
    if front_is_clear():
        move()
    else:
        jump()
