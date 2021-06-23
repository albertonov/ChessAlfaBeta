import time


class Statistics(object):

    def __init__(self):
        self.generated = 0
        self.expanded = 0
        self.generated_per_move = 0
        self.expanded_per_move = 0
        self.init = time.time()
        self.final = 0
        self.total_time = 0
        self.time_per_movement = 0
        self.total_moves = 0

    def finalize(self):
        self.final = time.time()
        self.total_time = self.final - self.init
        self.time_per_movement = self.total_time / self.total_moves
        self.generated_per_move = self.generated_per_move / self.total_moves
        self.expanded_per_move = self.expanded_per_move / self.total_moves
