try:
    import pyperclip
except ImportError:
    pyperclip = None  # handle gracefully

SYMBOLS = "abcdefghijklmnopqrstuvwxyz"

while True:
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    response = input(">").lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    else:
        print("Please enter either 'e' for encrypt or 'd' for decrypt.")

while True:
    maxkey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxkey))
    response = input(">")
    if not response.isdecimal():
        continue

    key = int(response)
    if 0 <= key <= maxkey:
        break

print('Enter the message to {}:'.format(mode))
message = input('> ').lower()  # match SYMBOLS which is lowercase

translated = ""
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        # Wrap around
        num %= len(SYMBOLS)
        translated += SYMBOLS[num]
    else:
        translated += symbol  # leave non-alphabetic characters as is

print("Result:", translated)

if pyperclip:
    try:
        pyperclip.copy(translated)
        print('Full {}ed text copied to clipboard.'.format(mode))
    except:
        pass
