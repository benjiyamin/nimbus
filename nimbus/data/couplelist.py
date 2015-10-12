
from nimbus.data import data
from nimbus.reports.report import show_couples_in_list
from .baselist import BaseList


class CoupleList(BaseList):

    def __init__(self, name, headers, list_=None):
        self.name = name
        self.headers = headers
        super(CoupleList, self).__init__(list_)

    def create(self, value1, value2, order=True):
        """Create a new couple and add it to the list."""
        new_couple = value1, value2
        self.list.append(new_couple)
        if order:
            self.order()
        self.show_all()
        return

    def copy(self, index, order=True):
        """Create a copy of the object at the specified index
        from the list and append it to the end of the list"""
        data.copy_from_list_and_print(index, self.list)
        if order:
            self.order()
        return

    def order(self, column=0):
        """Order the list by column."""
        self.list = sorted(self.list, key=lambda couple: couple[column])
        return

    def show_all(self):
        """Display all list stored in the list."""
        show_couples_in_list(self.name, self.headers, self.list)
        return
