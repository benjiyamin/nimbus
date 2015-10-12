
import copy
import csv


def delete_from_list_and_print(index, list_):
    thing = list_[index]
    list_.remove(thing)
    class_name = thing.__class__.__name__
    del thing
    print("\nSuccess: %s at index %s has been deleted.\n" % (class_name,  index))
    return


def copy_from_list_and_print(index, list_):
    object_ = list_[index]
    copy_object = copy.deepcopy(object_)
    class_name = copy_object.__class__.__name__
    list_.append(copy_object)
    print("\nSuccess: %s at index %s has been copied and appended to the list.\n" % (class_name,  index))
    return


def append_to_list_and_print(object_, list_):
    list_.append(object_)
    class_name = object_.__class__.__name__
    print('\nSuccess: New %s created.\n' % class_name)
    return


def couples_from_csv(filename):
    open_file = open(filename, "rt")
    reader = csv.reader(open_file, delimiter=',')
    tuple_list = []
    for row in reader:
        i = float(row[0])
        j = float(row[1])
        tuple_list.append((i, j))
    open_file.close()
    return tuple_list
