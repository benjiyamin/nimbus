
from .data import delete_from_list_and_print, copy_from_list_and_print, clear_list_and_print


class NimList:

    def __init__(self, _list=None):
        if _list:
            self.list = _list
        else:
            self.list = []

    def delete(self, index):
        """Remove the object at the specified index from the list and delete it."""
        delete_from_list_and_print(index, self.list)
        return

    def copy(self, index):
        """Create a copy of the object at the specified index
        from the list and append it to the end of the list"""
        copy_from_list_and_print(index, self.list)
        return

    def clear(self):
        """Remove all objects from the list and delete them."""
        clear_list_and_print(self.list, self.delete)
        return
