def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("C:\\Users\\shzahee\\Downloads\\python-ds-practice-solution\\python-ds-practice-solution\\fs_5_read_file_list\\dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """
    with open(filename) as f:
        for line in f:
            print(f'- {line.strip()}')
    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!