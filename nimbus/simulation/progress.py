
class ProgressBar:

    def __init__(self, length, start_message=None, end_message=None):
        self.length = length
        self.start_message = start_message
        self.end_message = end_message

    def begin(self):
        start_string = '\n'
        if self.start_message:
            start_string += self.start_message
        print(start_string)
        return

    def update(self, curr_step, total_steps):
        prog_hash = self.length * curr_step // total_steps
        print("[{}{}] {}%".format('#' * prog_hash, ' ' * (60 - prog_hash), curr_step * 100 // total_steps), end="\r")
        return

    def complete(self):
        self.update(1, 1)
        end_string = '\n'
        if self.end_message:
            end_string += self.end_message
        print(end_string)
        return
