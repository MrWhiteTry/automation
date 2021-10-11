#! python3
# mcb.pyw - Saves and load fragments of text in clipboard
# How to use: py.exe mcb.pyw save <key_word> -
#                 saves "Key_word" in clipboard
#             py.exe mcb.pyw <key_word> -
#                 Load "key_word" in clipboard
#             py.exe mcb.pyw list -
#                 load all key_words in clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save from clipboard
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # Create list of "key_words" and load it in clipboard.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
