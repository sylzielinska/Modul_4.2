def palindrom(text):
    '''
    Funcja sprawdza czy słowo podane jako argument
    pisane od lwewj do prawej
    i od prawej do lewej brzmi jest tożsame.
    
    '''
    return text == text[::-1]
if palindrom('inka'):
    print('yes')
else:
    print('no')