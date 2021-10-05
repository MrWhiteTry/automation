#! python 3
# Write function like a "strip()" but use only regex.
import re


def newStrip(text, symbol):
    if symbol == '':
        matches = re.sub(r'^(\s)*', '', text)
        matches = re.sub(r'(\s)*$', '', matches)
        print(matches)
    else:
        reg =r'^(' + delSome + r')*'''
        symbolsRegex = re.sub(reg, '', text)
        reg =r'(' + delSome + r')*$'''
        symbolsRegex1 = re.sub(reg, '', symbolsRegex)
        print(symbolsRegex1)


someText = str(input("input text" + '\n'))
delSome = str(input("input what you want to change" + '\n'))
newStrip(someText, delSome)
