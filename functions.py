
def get_todos(filepath="toDos.txt"):
    """ Read a txt file and return the list of to-do items """
    with open(filepath, "r") as local_file:
        local_todos = local_file.readlines()
    return local_todos # we need to return the list

def write_todos(todos_arg, filepath="toDos.txt"):
    """ Write to-do items list in a txt file, return None """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

# __name__ var is defined by Python and it's == "__main__" when you run the .py directly
# The code below doesn't get executed when run from a different .py
if __name__ == "__main__":
    print(get_todos())
