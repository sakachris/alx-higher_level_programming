#!/usr/bin/python3
"""

    String indentation

"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: . ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text2 = ""
    for c in text:
        if c in ['.', ':', '?']:
            text2 += c
            text2 += '\n\n'
        else:
            text2 += c
    text3 = ""
    for i, t in enumerate(text2):
        if t == ' ' and text2[i-1] == '\n':
            continue
        text3 += t

    return print(text3, end='')
