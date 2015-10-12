
from nimbus.data import data


class BaseList:

    def __init__(self, list_=None):
        if not list_:
            list_ = []
        self.list = list_

    def delete(self, index):
        """Remove the object at the specified index from the list and delete it."""
        data.delete_from_list_and_print(index, self.list)
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
