#! python3
# PassSeciur.py - Программа для не защищённого хранения паролей

PASSWORDS = {'email': 'F7min1BDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VnALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import pyperclip
import sys

if len(sys.argv) < 2:
    print('Использование: python PassSeciur.py [Имя учётной записи] - '
          'копирование пароля учётной записи')
    sys.exit()

account = sys.argv[1]  # первый аргумент командной строки - это
# имя учётной записи

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Пароль для ' + account + ' скопирован в буфер обмена.')
else:
    print('Учётная запись ' + account + 'отсутсвует в списке.')
