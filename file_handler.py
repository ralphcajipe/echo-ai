# File Handler function to read a file


def read(filename):
    """
    It opens a file, reads its contents, and returns the contents. Using an
    encoding of UTF-8 is how you can read a file containing emoji in Python.

    :param filename: the name of the file you want to read
    :return: The contents of the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
    return contents
