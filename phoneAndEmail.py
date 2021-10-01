#! python3
# phoneAndEmail.py - search phone numbers and e-mails in clipboard

import pyperclip, re
# Create Regex for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # terretorial code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 numders
    (\s|-|\.)?                      # separator
    (\d{4})                         # last 4 numbers
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # additional number
    )''', re.VERBOSE)               # ignore whitespace

#  Create Regex for emails
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+     # User name
    @                     # symbol @
    [a-zA-Z0-9.-]+        # Domen name
    (\.[a-zA-Z]{2,4})     # other part of adress
    )''', re.VERBOSE)

# Find match in text in clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[0] != '':
        phoneNum += ' x' + groups[0]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Cope result in clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Made copy in clipboard:')
    print('\n'.join(matches))
else:
    print('Fone numbers and emails not founded.')
