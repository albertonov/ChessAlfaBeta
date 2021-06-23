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
        self.init_eval = 0
        self.final_eval = 0
        self.delta = self.final_eval -self.init_eval

    def finalize(self):
        self.final = time.time()
        self.total_time = self.final - self.init
        self.time_per_movement = self.total_time / self.total_moves
        self.generated_per_move = round(self.generated / self.total_moves)
        self.expanded_per_move = round(self.expanded / self.total_moves)

    def show_me(self):
        print(f"States generated: {self.generated}")
        print(f"States expanded: {self.expanded}")
        print(f"Time required: {self.total_time:.2f}(s)")
        print(f"From initial eval[{self.init_eval}] to a final eval[{self.final_eval}] ")
        print(f"Per movement statistics:")
        print(f"\tTime per movement->{self.time_per_movement:.2f}(s)")
        print(f"\tGenerated states per movement->{self.generated_per_move}")
        print(f"\tExpanded states per movement->{self.expanded_per_move}")

