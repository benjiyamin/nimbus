
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

    def create_gutter(self, *args, **kwargs):
        """Create a gutter and add it to the link list."""
        self.create(Gutter, *args, **kwargs)
        return

    def create_channel(self, *args, **kwargs):
        """Create a channel and add it to the link list."""
        self.create(Channel, *args, **kwargs)
        return

    def all_channels(self):
        channels = self.get_all_from_class(Channel)
        return channels

    def all_inlets(self):
        inlets = self.get_all_from_class(Inlet)
        return inlets

    def all_gutters(self):
        gutters = self.get_all_from_class(Gutter)
        return gutters

    def get_all_from_class(self, class_):
        all_objects = [link for link in self.list if link.__class__ is class_]
        return all_objects

    def get_channel(self, index):
        all_channels = self.all_channels()
        channel = all_channels[index]
        return channel

    def get_inlet(self, index):
        all_inlets = self.all_inlets()
        inlet = all_inlets[index]
        return inlet

    def get_gutter(self, index):
        all_gutters = self.all_gutters()
        gutter = all_gutters[index]
        return gutter
