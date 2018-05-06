#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation
try:
    text_indentation((1,))
except Exception as e:
    print(e)
