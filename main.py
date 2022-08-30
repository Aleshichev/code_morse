alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
            '4', '5', '6', '7', '8', '9']
symbols = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
           '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
           '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--',
           '....-', '.....', '-....', '--...', '---..', '----.']


def del_gap(text_sentense):
    """The function removes extra spaces. Creates and return a new list"""
    new_sentense = []
    for text in text_sentense:
        if text != '':
            new_sentense.append(text)
    return new_sentense


def morse_decode(alphabet, symbols, new_sentense):
    """The function decodes the cipher and print new tetx"""
    morze_text = ''
    for letter in new_sentense:
        index_letter = symbols.index(letter)
        new_letter = alphabet[index_letter]
        morze_text += new_letter + " "
    print(f"Your decode morze text is\n{morze_text}")

def morse_encode(alphabet, symbols, new_sentense):
    """The function encrypts the text and print new text"""
    morze_text = ''
    for text in new_sentense:
        for letter in text:
            if letter in alphabet:
                index_letter = alphabet.index(letter)
                new_letter = symbols[index_letter]
                morze_text += new_letter + '  '
            else:
                morze_text += ''
        morze_text += '       '
    print (f"Your morze text is\n{morze_text}")


loop = 0
end_program = True
while end_program:
    if loop == 0:
        ask = (input("Let's start. Yes/no:")).lower()
        loop += 1
    else:
        ask = (input("Once again. Yes/no:")).lower()
        loop += 1
    if ask == "yes":
        choice = (input(f"What do you want? Please write (encode/decode):")).lower()
        text_sentense = input(f'Please enter the text:').lower().split(" ")
        new_text = del_gap(text_sentense)
        if choice == 'encode':
            morse_encode(alphabet, symbols, new_text)
        elif choice == 'decode':
            morse_decode(alphabet, symbols, new_text)
        else:
            print("Some mistake. Check (encode/decode) above")
    else:
        print("Ok. Bye!")
        end_program = False




