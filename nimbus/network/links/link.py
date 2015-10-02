

class Link:

    def __init__(self, node1=None, node2=None, shape=None):
        self.node1 = node1
        self.node2 = node2
        self.shape = shape

    def get_flow(self, stage1, stage2):
        flow = 0.0
        return flow

    def get_flow_area(self, depth):
        """Return the flow area in square feet."""
        if self.shape:
            flow_area = self.shape.get_flow_area(depth)
        else:
            flow_area = 0.0
        return flow_area
