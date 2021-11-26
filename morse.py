# morse.py
# pylint: disable=missing-docstring

def decode(message):
    alphabet = {
        "": "",
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        "... --- ...": "SOS"
    }
    answer = ""

    words = message.split(" / ")

    for word in words:
        for letter in word.split(" "):
            answer += alphabet[letter]
        answer += " "
    answer = answer.strip()

    return answer    

