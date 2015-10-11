
from .data import delete_from_list_and_print, copy_from_list_and_print
from nimbus.reports.report import show_couples_in_list


class CoupleList:

    def __init__(self, name, headers, list_=None):
        self.name = name
        self.headers = headers
        if not list_:
            list_ = []
        self.list = list_

    def create(self, value1, value2):
        """Create a new couple and add it to the list."""
        new_couple = value1, value2
        self.list.append(new_couple)
        self.order()
        self.show_all()
        return

    def order(self, column=0):
        """Order the list by column."""
        self.list = sorted(self.list, key=lambda couple: couple[column])
        return

    def show_all(self):
        """Display all list stored in the list."""
        show_couples_in_list(self.name, self.headers, self.list)
        return

    def delete(self, index):
        """Remove the object at the specified index from the list and delete it."""
        delete_from_list_and_print(index, self.list)
        return

    def copy(self, index):
        """Create a copy of the object at the specified index
        from the list and append it to the end of the list"""
        copy_from_list_and_print(index, self.list)
        return

    def get(self, index):
        object_ = self.list[index]
        print('\nSuccess: %s object assigned to variable.\n' % object_.__class__.__name__)
        return object_

    def all(self):
        objects = self.list
        return objects

    def enumerate(self):
        tuples = enumerate(self.list)
        return tuples

    def length(self):
        length = len(self.list)
        return length
