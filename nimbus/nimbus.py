
import pickle
import os
from nimbus.project import Project


class Nimbus:

    def __init__(self):
        self.project = None
        self.filepath = ''
        print("\nSuccess: Nimbus is loaded and ready to go.\n")

    def new_project(self):
        """Create a project and set it as nimbus's project."""
        new_project = Project()
        self.project = new_project
        print("\nSuccess: New project created.\n")
        return

    def save_project(self, filepath=None):
        """Pickle project object to a save file"""
        if filepath is None:
            try:
                open_file = open(self.filepath, "wb")
            except:
                raise ValueError("\nFile path '%s' not found. Define a filename.\n" % self.filepath)
        else:
            if ".npf" in filepath:
                pass
            elif "." in filepath:
                raise ValueError("Filename must have '.npf' extension!")
            else:
                filepath += ".npf"
            open_file = open(filepath, "wb")
            self.filepath = os.path.abspath(filepath)
        pickle.dump(self.project, open_file)
        open_file.close()
        print("\nSuccess: Project saved to '%s'\n" % self.filepath)
        return

    def load_project(self, filepath):
        """Unpickle project object from a save file"""
        try:
            open_file = open(filepath, "rb")
            project = pickle.load(open_file)
        except:
            raise ValueError("Not a valid file!")
        open_file.close()
        self.project = project
        self.filepath = os.path.abspath(filepath)
        print("\nSuccess: Project loaded from '%s'\n" % self.filepath)
        return
