#!/usr/bin/python3
def remove_char_at(str, n):
    idx = len(str)
    if (n >= 0 and n < idx):
        return (str.replace(str[n], ''))
    else:
        return str
