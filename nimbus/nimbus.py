
import pickle
import os
from nimbus.project import Project


class Nimbus:

    def __init__(self):
        self.project = None
        self.filepath = ''
        print("Success: Nimbus is locked and loaded.")

    def new_project(self, directory):
        """Create a project with the defined directory, set it as nimbus's project, and return the object."""
        new_project = Project(directory)
        self.project = new_project
        print("Success: New project created.")
        return new_project

    def save_project(self, filepath=None):
        """Pickle project object to a save file"""
        #os.chdir(self.project.directory)
        if not filepath:
            try:
                open_file = open(self.filepath, "wb")
            except:
                raise ValueError("File path " + self.filepath + " not found. Define a filename.")
            log_filepath = self.filepath
        else:
            if ".npf" in filepath:
                pass
            elif "." in filepath:
                raise ValueError("Filename must have '.npf' extension!")
            else:
                filepath += ".npf"
            log_filepath = filepath
            open_file = open(filepath, "wb")
        pickle.dump(self.project, open_file)
        open_file.close()
        print('Success: Project saved to ' + log_filepath)
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
        self.filepath = filepath
        print('Success: Project loaded from ' + filepath)
        return
