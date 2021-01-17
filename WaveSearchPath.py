import pygame
from copy import deepcopy
from collections import deque


def level_to_search(level, walls):
    level = deepcopy(level)
    width = len(level[0])
    height = len(level)
    for i in range(height):
        for j in range(width):
            val = level[i][j]
            if val in walls:
                level[i][j] = -1


class WaveSearchPath:
    def search(self, start_pos, end_pos, board, wall=-1):
        self.set_init_data(start_pos, end_pos, board, wall)
        self.emit()
        path = self.get_path()
        return path

    def set_init_data(self, start_pos, end_pos, board, wall):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.wall = wall
        self.board = deepcopy(board)
        self.width = len(board[0])
        self.height = len(board)

    def emit(self):
        q = deque()
        q.append(self.start_pos)
        self.mark_wave(self.start_pos, 1)
        while len(q):
            current = q.popleft()
            if self.is_finish(current):
                break
            i, j = current
            neighbors = self.get_neighbors(current)
            self.mark_wave_list(neighbors, self.board[i][j] + 1)
            q.extend(neighbors)

    def get_path(self):
        end_pos_i, end_pox_j = self.end_pos
        end_pos_val = self.board[end_pos_i][end_pox_j]
        if end_pos_val == 0:
            return None
        path = []
        item = self.end_pos
        path.append(item)
        while item != self.start_pos:
            item_i, item_j = item
            item_val = self.board[item_i][item_j]
            neighbors = self.get_neighbors(item, need_visited=True)
            for pos in neighbors:
                i, j = pos
                neighbor_val = self.board[i][j]
                if neighbor_val == item_val - 1:
                    item = pos
                    path.append(item)
        return list(reversed(path))

    def get_neighbors(self, pos, need_visited=False):
        i, j = pos
        return self.filter_invalid_pos([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)], need_visited)

    def filter_invalid_pos(self, pos_list, need_visited):
        result = []
        for pos in pos_list:
            i, j = pos
            if 0 <= i < self.height and 0 <= j < self.width and not self.is_wall(pos):
                if need_visited:
                    result.append(pos)
                else:
                    if not self.is_visited(pos):
                        result.append(pos)
        return result

    def is_wall(self, pos):
        i, j = pos
        return self.board[i][j] == self.wall

    def is_visited(self, pos):
        i, j = pos
        return self.board[i][j] > 0

    def is_finish(self, pos):
        return pos == self.end_pos

    def mark_wave(self, pos, wave_number):
        i, j = pos
        self.board[i][j] = wave_number

    def mark_wave_list(self, pos_list, wave_number):
        for pos in pos_list:
            self.mark_wave(pos, wave_number)
