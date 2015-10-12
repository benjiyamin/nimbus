

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
    
    def get_current_percentage(self, curr_step, total_steps):
        curr_percentage = curr_step * 100 // total_steps
        return curr_percentage 

    def update(self, curr_step, total_steps):
        prog_hash = self.length * curr_step // total_steps
        print("[{}{}] {}%".format('#' * prog_hash, ' ' * (self.length - prog_hash), self.get_current_percentage(curr_step, total_steps)), end="\r")
        return

    def complete(self):
        self.update(1, 1)
        end_string = '\n'
        if self.end_message:
            end_string += self.end_message
        print(end_string)
        return
