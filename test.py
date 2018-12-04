def pr(string):
    print(string)


def fu(string):
    print(string)


cmd_dict = {
    1: pr,
    2: fu
}

cmd_dict[1]("wayne")
