#!/usr/bin/python3
"""Module docstring
This module contains a function that prints a text
with 2 newlines after the following characters: . ? :
"""


def text_indentation(text):
    """Function docstring
    text_indentation: prints 2 newlines after ? . :
    Args:
        text: text to indent"""
    if isinstance(text, float) or isinstance(text, int):
        raise TypeError('text must be a string')
    if any(type(el) for el in text) != str:
        raise TypeError('text must be a string')
    try:
        nl = [w for w in text]
        for i in range(len(nl)):
            if nl[i] == '.' or nl[i] == '?' or nl[i] == ':':
                if nl[i + 1] == ' ' and nl[i + 2] != ' ':
                    nl[i + 1] = '\n\n'
                elif nl[i + 1] == ' ' and nl[i + 2] == ' ':
                    nl[i + 1] ='\n\n'
                    nl[i + 2] = ""
    except:
        raise TypeError('text must be a string')
    finally:
        print(''.join(map(str, nl)))
