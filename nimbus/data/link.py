
from . import object as ob
from nimbus.network.links.link import Link
from nimbus.network.links.pipe import Pipe
from nimbus.network.links.weir import Weir
from nimbus.network.links.inlet import Inlet
from nimbus.network.links.gutter import Gutter
from nimbus.network.links.channel import Channel


class LinkList(ob.ObjectList):

    def __init__(self, list_=None):
        super(LinkList, self).__init__(Link, list_, True)
        self.pipes = []
        self.weirs = []
        self.inlets = []
        self.gutters = []
        self.channels = []

    def create_pipe(self, *args, **kwargs):
        """Create a pipe and add it to the link list."""
        self.create(Pipe, *args, **kwargs)
        self.pipes.append(self.list[-1])
        return

    def create_weir(self, *args, **kwargs):
        """Create a weir and add it to the link list."""
        self.create(Weir, *args, **kwargs)
        self.weirs.append(self.list[-1])
        return

    def create_inlet(self, *args, **kwargs):
        """Create an inlet and add it to the link list."""
        self.create(Inlet, *args, **kwargs)
        self.inlets.append(self.list[-1])
        return

    def create_gutter(self, *args, **kwargs):
        """Create a gutter and add it to the link list."""
        self.create(Gutter, *args, **kwargs)
        self.gutters.append(self.list[-1])
        return

    def create_channel(self, *args, **kwargs):
        """Create a channel and add it to the link list."""
        self.create(Channel, *args, **kwargs)
        self.channels.append(self.list[-1])
        return

    def delete_pipe(self, index):
        """Remove the object at the specified index from the list and delete it."""
        object_ = self.pipes[index]
        self.pipes.remove(object_)
        list_index = self.list.index(object_)
        self.delete(list_index)
        return
    
    def delete_weir(self, index):
        """Remove the object at the specified index from the list and delete it."""
        object_ = self.weirs[index]
        self.weirs.remove(object_)
        list_index = self.list.index(object_)
        self.delete(list_index)
        return
    
    def delete_inlet(self, index):
        """Remove the object at the specified index from the list and delete it."""
        object_ = self.inlets[index]
        self.inlets.remove(object_)
        list_index = self.list.index(object_)
        self.delete(list_index)
        return
    
    def delete_gutter(self, index):
        """Remove the object at the specified index from the list and delete it."""
        object_ = self.gutters[index]
        self.gutters.remove(object_)
        list_index = self.list.index(object_)
        self.delete(list_index)
        return
    
    def delete_channel(self, index):
        """Remove the object at the specified index from the list and delete it."""
        object_ = self.channels[index]
        self.channels.remove(object_)
        list_index = self.list.index(object_)
        self.delete(list_index)
        return

