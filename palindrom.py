string = "bring"


def palindrom(string):
    return string == string[::-1]


print(palindrom(string))
