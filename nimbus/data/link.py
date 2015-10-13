
from . import object as ob
from nimbus.network import links


class LinkList(ob.ObjectList):

    def __init__(self, list_=None):
        super(LinkList, self).__init__(links.Link, list_, True)

    def create_pipe(self, *args, **kwargs):
        """Create a pipe and add it to the link list."""
        self.create(links.Pipe, *args, **kwargs)
        return

    def create_weir(self, *args, **kwargs):
        """Create a weir and add it to the link list."""
        self.create(links.Weir, *args, **kwargs)
        return

    def create_inlet(self, *args, **kwargs):
        """Create an inlet and add it to the link list."""
        self.create(links.Inlet, *args, **kwargs)
        return
