
from .data import delete_from_list_and_print, copy_from_list_and_print, append_to_list_and_print
from nimbus.reports.report import show_objects_in_list


class NimList:

    def __init__(self, class_, list_=None, display_class=False):
        self.class_ = class_
        if not list_:
            list_ = []
        self.list = list_
        self.display_class = display_class

    def create(self, from_class=None, *args, **kwargs):
        """Create a new object and add it to the list."""
        if from_class:
            new_object = from_class(*args, **kwargs)
        elif self.class_:
            new_object = self.class_(*args, **kwargs)
        else:
            raise ValueError
        append_to_list_and_print(new_object, self.list)
        return

    def add_from(self, index, list_):
        """Add object at specified index in specified list it to the list."""
        object_ = list_[index]
        append_to_list_and_print(object_, self.list)
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

    def show_all(self, from_class=None):
        """Display all object names stored in the list."""
        if from_class:
            show_objects_in_list(from_class.__name__ + 's', self.list, self.display_class)
        elif self.class_:
            show_objects_in_list(self.class_.__name__ + 's', self.list, self.display_class)
        else:
            raise ValueError
        return

    def all(self):
        objects = self.list
        return objects

    def enumerate(self):
        tuples = enumerate(self.list)
        return tuples

    def length(self):
        length = len(self.list)
        return length
