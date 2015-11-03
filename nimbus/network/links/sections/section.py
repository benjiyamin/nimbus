

class Section:

    def __init__(self, horizontal):
        self.horizontal = horizontal

    def get_flow_area(self, depth):
        flow_area = 0.0
        return flow_area

    def get_wet_perimeter(self, depth):
        wet_perimeter = 0.0
        return wet_perimeter

    def get_equivalent_head(self, depth):
        equivalent_head = 0.0
        return equivalent_head

    def get_hyd_radius(self, depth):
        area = self.get_flow_area(depth)
        perimeter = self.get_wet_perimeter(depth)
        hyd_radius = area / perimeter
        return hyd_radius
