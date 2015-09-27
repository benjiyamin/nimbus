
import copy


def clear_list_and_print(_list, delete_function):
    for i, thing in enumerate(_list):
        delete_function(i)
    return


def delete_from_list_and_print(index, _list):
    thing = _list[index]
    _list.remove(thing)
    class_name = thing.__class__.__name__
    del thing
    print("\nSuccess: %s at index %s has been deleted.\n" % (class_name,  index))
    return


def copy_from_list_and_print(index, _list):
    thing = _list[index]
    copy_thing = copy.deepcopy(thing)
    class_name = copy_thing.__class__.__name__
    _list.append(copy_thing)
    print("\nSuccess: %s at index %s has been copied and appended to the list.\n" % (class_name,  index))
    return


def append_to_list_and_print(_object, _list):
    _list.append(_object)
    class_name = _object.__class__.__name__
    print('\nSuccess: New %s created.\n' % class_name)
    return