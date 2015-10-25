

class Matrix:

    def __init__(self, rows):
        self.rows = rows

    def get(self, row, column):
        value = self.rows[row][column]
        return value
