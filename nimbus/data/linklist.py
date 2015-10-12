
from nimbus.network.links import Link, Pipe, Weir, Inlet
from .objectlist import ObjectList


class LinkList(ObjectList):

    def __init__(self, list_=None):
        super(LinkList, self).__init__(Link, list_, True)

    def create_pipe(self, *args, **kwargs):
        """Create a pipe and add it to the link list."""
        self.create(Pipe, *args, **kwargs)
        return

    def create_weir(self, *args, **kwargs):
        """Create a weir and add it to the link list."""
        self.create(Weir, *args, **kwargs)
        return

    def create_inlet(self, *args, **kwargs):
        """Create an inlet and add it to the link list."""
        self.create(Inlet, *args, **kwargs)
        return
