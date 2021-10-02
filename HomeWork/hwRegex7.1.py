#! python 3
# This file is my homework from AutoBoringStuff page 217

# 1st task - write function for chek "Strong passwords"
import re

passwords = '666u666H'

strongRegex = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$')
matches = strongRegex.search(passwords)
print(matches)
