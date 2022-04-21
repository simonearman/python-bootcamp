def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    # If there is a wall in front, turn left so the robot has the wall on his right
    if wall_in_front():
        turn_left()
    # If the front is clear and the robot has a wall on his right, move
    elif wall_on_right():
        move()
        # While walking the robot loses the wall on his right, keep turning right until he finds the wall again
        # Unless he finds the goal
        while right_is_clear() and not at_goal():
            turn_right()
            move()
    # If there is no wall in front and no wall on the right, keep walking
    else:
        move()
