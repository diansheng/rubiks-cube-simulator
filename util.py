index_2_color = 'null blue yellow red green white violet'.split()
color_2_index = {c:i for i,c in enumerate(index_2_color)}
index_2_side = 'back, front, left, right, bottom, top'.split(', ')
side_2_index = {c: i for i, c in enumerate(index_2_side)}


side_2_vec = {
    'back': (-1,0,0),
    'front': (1,0,0),
    'left': (0,-1,0),
    'right': (0,1,0),
    'bottom': (0,0,-1),
    'top': (0,0,1),
}

def colored_string_by_index(index):
    index_2_code = {
        1: '\x1b[6;30;44m',  # blue
        2: '\x1b[6;30;43m',  # yellow
        3: '\x1b[6;30;41m',  # red
        4: '\x1b[6;30;42m',  # green
        5: '\x1b[6;30;47m',  # white
        6: '\x1b[6;30;45m',  # violet
    }
    return index_2_code[index] + str(index) + '\x1b[0m'

