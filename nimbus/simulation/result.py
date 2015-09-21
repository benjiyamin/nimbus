
import pickle


class Result:

    def __init__(self, nodes, links):
        self.nodes = nodes
        self.links = links

    def write(self, path):
        """Pickle self to a save file"""
        if ".nrf" in self.path:
            path = self.path
        elif "." in self.path:
            raise ValueError("Filename must have '.nrf' extension!")
        else:
            path = self.path + ".npf"
        open_file = open(path, "wb")
        pickle.dump(self, open_file)
        open_file.close()
        return
