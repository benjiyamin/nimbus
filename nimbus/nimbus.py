
import pickle
import os
from nimbus.project import Project


class Nimbus:

    def __init__(self):
        self.project = None

    def new_project(self, directory):
        """Create a project with the defined directory, set it as nimbus's project, and return the object."""
        new_project = Project(directory)
        self.project = new_project
        return new_project

    def save_project(self, filename):
        """Pickle project object to a save file"""
        os.chdir(self.project.directory)
        if ".npf" in filename:
            filename = filename
        elif "." in filename:
            raise ValueError("Filename must have '.npf' extension!")
        else:
            filename += ".npf"
        open_file = open(filename, "wb")
        pickle.dump(self.project, open_file)
        open_file.close()
        return

    def load_project(self, filepath):
        """Unpickle project object from a save file"""
        try:
            open_file = open(filepath, "rb")
            new_project = pickle.load(open_file)
        except:
            raise ValueError("Not a valid file!")
        open_file.close()
        return new_project
