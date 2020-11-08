
# Rubik's cube.
# user control by command operation
# current state is presented in console as well
# color in console is represented in numbers


# from util import *
from classes import Cell, Cube


def ask_for_next_step():
    print("rotate Rubik's Cube, key in action number and hit Enter >>> ")
    print("""Please key in commands in the format of <action>.<layer>
    Actions:
        a: turn clock-wise
        b: turn anti-clock-wise
        c: turn left
        d: turn right
        e: rotate inwards from the top
        f: rotate outwards from the top

    Layers:
        1: top/right/front layer
        2: middle layer
        3: bottom/left/back layer

        0 End game
    """)
    # print("""
    #     a.1 turn clock-wise the front layer
    #     a.2 turn clock-wise the center layer
    #     a.3 turn clock-wise the back layer
    #
    #     b.1 turn anti-clock-wise the front layer
    #     b.2 turn anti-clock-wise the center layer
    #     b.3 turn anti-clock-wise the back layer
    #
    #     c.1 turn left the top layer
    #     c.2 turn left the center layer
    #     c.3 turn left the bottom layer
    #
    #     d.1 turn right the top layer
    #     d.2 turn right the center layer
    #     d.3 turn right the bottom layer
    #
    #     e.1 rotate inwards the right layer
    #     e.2 rotate inwards the center layer
    #     e.3 rotate inwards the left layer
    #
    #     f.1 rotate outwards the right layer
    #     f.2 rotate outwards the center layer
    #     f.3 rotate outwards the left layer
    #
    #     0 End game
    # """)
    action = str(input())

    actions = 'a.1,a.2,a.3,b.1,b.2,b.3,c.1,c.2,c.3,d.1,d.2,d.3,e.1,e.2,e.3,f.1,f.2,f.3'.split(',')

    if action == '0':
        print("Game ended")
        return None
    elif action not in actions:
        print('the action is not valid. Action code in the format of "<alphabet>.<digit>". Please try again.')
        return ask_for_next_step()
    else:
        return action


if __name__=='__main__':
    print('game start >>>')

    cube = Cube()
    cube.draw_cube()

    x = ask_for_next_step()
    while x:
        print('='*30 + 'before' + '='*30)
        cube.draw_cube()

        cube.rotate(action=x)

        print('=' * 30 + 'after' + '=' * 30)
        cube.draw_cube()
        #
        # for coor, cell in cube.cells.items():
        #     if coor[0] == 1:
        #         print(cell.name)

        x = ask_for_next_step()
