# pos project
# Invoice maker

import time, datetime

while True:
    file1 = 'Invoice_card.txt'
    with open(file1) as file_object: # html 파일 읽기, with 문을 벗어나면 파일은 자동으로 close 된다.
        invo_card = file_object.read()
    file2 = 'Invoice_cash.txt'
    with open(file2) as file_object:
        invo_cash = file_object.read()