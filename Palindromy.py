def palindrom(text):
    return text == text[::-1]
if palindrom('inka'):
    print('yes')
else:
    print('dupa')