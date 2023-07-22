def reverse_string(string):
    str = ""
    for i in string:
        str = i + str
    return str
    string = "Holberton"
    print(reversed(string))