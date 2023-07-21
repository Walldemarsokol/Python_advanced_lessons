text = input('enter text: ')
if text.isnumeric():
    text = int(text)
    print(bin(text))
    print(oct(text))
    print(hex(text))
elif text.isascii():
    print("text is written by ASCII")
else:
    print("written by her kak")