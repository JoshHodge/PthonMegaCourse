def len_str(lstring):
    if type(lstring) == int:
        return "That is an integer not a string"
    elif type(lstring) == float:
        return "That is a float not a string"
    else:
        return len(lstring)
