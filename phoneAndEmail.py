#! python3
# phoneAndEmail.py - search phone numbers and e-mails in clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # terretorial code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 numders
    (\s|-|\.)?                      # separator
    (\d{4})                         #  last 4 numbers
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # additional number
    )''', re.VERBOSE)               # ignored whitespace

# TODO: create Regex for emails

# TODO: find match in text in clipboard

# TODO: Cope result in clipboard

