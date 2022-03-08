def to_morse_code(string):
    converters={'A':".-",
                'B':'-...',
                'C':'-.-.',
                'D':'-..',
                'E':'.',
                'F':'..-.',
                'G':'--.',
                'H':'....',
                'I':'..',
                'J':'.---',
                'K':'-.-',
                'L':'.-..',
                'M':'--',
                'N':'-.',
                'O':'---',
                'P':'.--.',
                'Q':'--.-',
                'R':'.-.',
                'S':'---',
                'T':'-',
                'U':'..-',
                'V':'...-',
                'W':'.--',
                'X':'-..-',
                'Y':'-.--',
                'Z':'--..',
                ' ':' '}
    new_list=[converters[x.upper()] for x in string]
    return ''.join(new_list)

print('Welcome to Morse code converter !')
inp=input('Enter  "s" to start: ').upper()
if inp=='S':
    run=True
else:
    run=False
    print("Have a nice day!")

while run:
    str_to_convert=input('Enter the string to convert: ')
    output=to_morse_code(str_to_convert)
    print(f"The required morse code is {output}")
    response=input("To convert again press 'a' to quit press 'q': ").upper()
    if response=='A':
        continue
    run=False