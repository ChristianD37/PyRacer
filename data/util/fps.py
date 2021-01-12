import time

class MaxSizeList():

    def __init__(self, max_length):
        self.max_length = max_length
        self.ls = []

    def push(self, st):
        if len(self.ls) == self.max_length:
            self.ls.pop(0)
        self.ls.append(st)

    def get_list(self):
        return self.ls

#Class used as a replacement to Pygames clock. Uses python time module for extra precision
class FPS():
    # Takes in one argument, which limits the FPS. If nothing is entered, will use as much of the CPU as is available
    def __init__(self, cap = 0):
        self.previous_time = time.time()
        self.times_taken = MaxSizeList(50)
        self.fps = 0
        self.cap = cap
        self.delay_limit = 0
        if cap > 0:
            self.delay_limit = 1/ self.cap

    # Main function that computes elapsed time since each frame and returns delta time value
    def get_delta_time(self, target_fps):
        elapsed_time  = self.elapsed_time()
        return  elapsed_time* target_fps

    # Helper function
    def elapsed_time(self):
        now = time.time()
        elapsed_time = now - self.previous_time
        self.previous_time = now
        delay = self.cap_fps(elapsed_time, self.cap)
        if elapsed_time: self.fps = 1.0/(delay + elapsed_time)
        self.times_taken.push(self.fps)
        return elapsed_time

    # Helper function. If a cap is specified, sleeps for appropriate time
    def cap_fps(self,elapsed_time, cap = 0 ):
        delay = 0
        if cap:
            delay = max(self.delay_limit - elapsed_time, 0)
            time.sleep(delay)
        return delay

    def get_fps(self):
        fps = sum(self.times_taken.get_list()) / len(self.times_taken.get_list())
        return fps