#! python3
# This program read a "txt" file and search in him the key-words
# next program give to user change key-words to him words or strings
# next "txt" file saves with changed string and changed string print on display

import re

changeText = open('text.txt')
fileText = changeText.read()
changeText.close()
mach = True

while True:
    if 'ADJECTIVE' in fileText:
        newAdjective = str(input("input some adjective:\n"))
        fileText = re.sub(r'ADJECTIVE', newAdjective, fileText)
    elif 'NOUN' in fileText:
        newNoun = str(input("input some noun:\n"))
        fileText = re.sub(r'NOUN', newNoun, fileText)
    elif 'ADVERB' in fileText:
        newAdverb = str(input("input some adverb:\n"))
        fileText = re.sub(r'ADVERB', newAdverb, fileText)
    elif 'VERB' in fileText:
        newVerb = str(input("input some verb:\n"))
        fileText = re.sub(r'VERB', newVerb, fileText)
    else:
        break
changeText = open('text.txt', 'w')
print(fileText)
changeText.write(fileText)
changeText.close()