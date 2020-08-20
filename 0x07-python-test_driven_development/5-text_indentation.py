#!/usr/bin/python3
"""Indentation module"""


def text_indentation(text):
    """
    indent text
    text: string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print(i, end='')
        if i == '.' or i == ':' or i == '?':
            print('\n')
