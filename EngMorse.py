english_to_morse = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
}
morse_to_english = {v: k for k, v in english_to_morse.items()}

input_text = input("Enter a text: ")

def decode(morse_text):
    for keys, values in morse_to_english.items():
        if morse_text == keys:
            morse_text = values
    return morse_text

def encode(english_text):
    for keys, values in english_to_morse.items():
        if english_text == keys:
            english_text = values
    return english_text

input_text = input_text.split(' ')
if input_text[0].isalpha() == True:
    for i in range(0, len(input_text)):
        input_text[i] = encode(input_text[i])
else:
    for i in range(0, len(input_text)):
        input_text[i] = decode(input_text[i])
result = ' '.join(input_text) # Your encoded/decoded answer should be assigned to 'result' variable

print(result)
