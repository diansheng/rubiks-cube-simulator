from util import *
import numpy as np
from collections import Counter

class Cell(object):
    def __init__(self, colors=None):
        '''
        colors: a list of color index, define color in the order of back, front, left, right, bottom, top
        '''
        colors = colors or ['null']*6
        self.colors = {side_2_vec[side]:c for side,c in zip(index_2_side,colors)}
        self.name=""

    def get_color(self, side):
        return self.colors[side_2_vec[side]]

    def get_color_index(self, side):
        return color_2_index[self.colors[side_2_vec[side]]]

    def set_color(self, side, color):
        self.colors[side_2_vec[side]] = color

    def rotate(self, transform_matrix):
        # print('[debug] previous colors')
        # print(self.colors)

        self.colors = {
            tuple(np.matmul(transform_matrix, np.array(vec).T).astype(int)):c
            for vec,c in self.colors.items()
        }

class Cube:
    def __init__(self):
        self.cells = {
            (i,j,k):Cell()
            for i in range(-1,2)
            for j in range(-1,2)
            for k in range(-1,2)
        }
        self.set_complete_color()

    def set_complete_color(self):
        colors = index_2_color[1:]
        sides = index_2_side

        for i in range(-1, 2):
            for j in range(-1,2):
                # color 6 sizes in the order of back, front, left, right, bottom, top
                self.cells[(-1, i, j)].set_color(sides[0],colors[0])
                self.cells[(1, i, j)].set_color(sides[1],colors[1])
                self.cells[(i, -1, j)].set_color(sides[2],colors[2])
                self.cells[(i, 1, j)].set_color(sides[3],colors[3])
                self.cells[(i, j, -1)].set_color(sides[4],colors[4])
                self.cells[(i, j, 1)].set_color(sides[5],colors[5])

        # check total number of colors
        color_count = Counter()
        for coor, cell in self.cells.items():
            for i in range(6):
                color_count[cell.get_color(sides[i])] += 1
                cell.name='_'.join(map(str,coor))
        print('Check color assignment')
        print(color_count)

    def reset(self):
        pass

    def draw_cube(self):
        """draw cube in the console"""
        # first top set
        e = color_2_index['null']
        out_stream = []
        out_stream.append([e, e] + [self.cells[(-1, i, 1)].get_color_index('top') for i in range(-1,2)])
        out_stream.append([e] + [self.cells[(0, i, 1)].get_color_index('top') for i in range(-1,2)] +
                          [e, self.cells[(-1, 1, 1)].get_color_index('right')])
        out_stream.append([self.cells[(1, i, 1)].get_color_index('top') for i in range(-1,2)]
                          + [e,
                             self.cells[(0, 1, 1)].get_color_index('right'),
                             self.cells[(-1, 1, 0)].get_color_index('right')])
        out_stream.append([self.cells[(1, i, 1)].get_color_index('front') for i in range(-1,2)]
                          + [self.cells[(1, 1, 1)].get_color_index('right'),
                             self.cells[(0, 1, 0)].get_color_index('right'),
                             self.cells[(-1, 1, -1)].get_color_index('right')
                             ])
        out_stream.append([self.cells[(1, i, 0)].get_color_index('front') for i in range(-1,2)]
                          + [self.cells[(1, 1, 0)].get_color_index('right'),
                             self.cells[(0, 1, -1)].get_color_index('right')
                             ])
        out_stream.append([self.cells[(1, i, -1)].get_color_index('front') for i in range(-1,2)]
                          + [self.cells[(1, 1, -1)].get_color_index('right')])

        for l in out_stream:
            print(' '.join([colored_string_by_index(x) if x!=0 else ' ' for x in l]))

    def rotate(self, action):
        action_type=action[0]
        layer=int(action[-1])

        if action_type=="a":
            cell_coordinates = [(2-layer, i, j) for i in range(-1,2) for j in range(-1,2)]
            transform_matrix = np.array([
                [1, 0, 0],
                [0, 0, 1],
                [0, -1, 0],
            ])
        elif action_type == 'b':
            cell_coordinates = [(2 - layer, i, j) for i in range(-1, 2) for j in range(-1, 2)]
            transform_matrix = np.array([
                [1, 0, 0],
                [0, 0, -1],
                [0, 1, 0],
            ])
        elif action_type == 'c':
            cell_coordinates = [(i, j, 2 - layer) for i in range(-1, 2) for j in range(-1, 2)]
            transform_matrix = np.array([
                [0, 1, 0],
                [-1, 0, 0],
                [0, 0, 1],
            ])
        elif action_type == 'd':
            cell_coordinates = [(i, j, 2 - layer) for i in range(-1, 2) for j in range(-1, 2)]
            transform_matrix = np.array([
                [0, -1, 0],
                [1, 0, 0],
                [0, 0, 1],
            ])
        elif action_type == 'e':
            cell_coordinates = [(i, 2 - layer, j) for i in range(-1, 2) for j in range(-1, 2)]
            transform_matrix = np.array([
                [0, 0, -1],
                [0, 1, 0],
                [1, 0, 0],
            ])
        elif action_type == 'f':
            cell_coordinates = [(i, 2 - layer, j) for i in range(-1, 2) for j in range(-1, 2)]
            transform_matrix = np.array([
                [0, 0, 1],
                [0, 1, 0],
                [-1, 0, 0],
            ])

        # todo: other actions

        selected_cells = list(map(lambda x: self.cells[x], cell_coordinates))

        # transform cells to new positions
        cell_coordinates = np.array(cell_coordinates, dtype=np.int16)
        new_coordinates = np.matmul(cell_coordinates, transform_matrix.T).astype(int)

        # update new coordinates
        for new_co, cell in zip(new_coordinates, selected_cells):
            cell.rotate(transform_matrix)
            self.cells[tuple(new_co)]=cell

