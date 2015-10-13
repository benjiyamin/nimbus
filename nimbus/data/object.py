
from . import data, base
from nimbus.reports import report as rp


class ObjectList(base.BaseList):

    def __init__(self, class_, list_=None, display_class=False):
        self.class_ = class_
        super(ObjectList, self).__init__(list_)
        self.display_class = display_class

    def create(self, from_class=None, *args, **kwargs):
        """Create a new object and add it to the list."""
        if from_class:
            new_object = from_class(*args, **kwargs)
        elif self.class_:
            new_object = self.class_(*args, **kwargs)
        else:
            raise ValueError
        data.append_to_list_and_print(new_object, self.list)
        return

    def copy(self, index):
        """Create a copy of the object at the specified index
        from the list and append it to the end of the list"""
        data.copy_from_list_and_print(index, self.list)
        return

    def add_from(self, index, list_):
        """Add object at specified index in specified list it to the list."""
        object_ = list_[index]
        data.append_to_list_and_print(object_, self.list)
        return

    def show_all(self, from_class=None):
        """Display all object names stored in the list."""
        if from_class:
            rp.show_objects_in_list(from_class.__name__ + 's', self.list, self.display_class)
        elif self.class_:
            rp.show_objects_in_list(self.class_.__name__ + 's', self.list, self.display_class)
        else:
            raise ValueError
        return
