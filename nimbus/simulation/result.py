
import pickle


class Result:

    def __init__(self, nodes, links):
        self.nodes = nodes
        self.links = links

    def write(self, filepath):
        """Pickle self to a save file"""
        if ".nrf" in filepath:
            filepath = filepath
        elif "." in filepath:
            raise ValueError("Filename must have '.nrf' extension!")
        else:
            filepath += ".nrf"
        open_file = open(filepath, "wb")
        pickle.dump(self, open_file)
        open_file.close()
        return

    @staticmethod
    def load(self, filepath):
        """Unpickle result object from a save file"""
        try:
            open_file = open(filepath, "rb")
            result = pickle.load(open_file)
        except:
            raise ValueError("Not a valid file!")
        open_file.close()
        return result
