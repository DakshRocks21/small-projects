import json
MORSE_CODE_DICT = json.load(open("morse.json"))
class Morse():
    def encode(self, message):
        message = message.upper()
        cipher = ""
        for letter in message:
            if letter != " ":
                cipher += MORSE_CODE_DICT[letter] + " "
            else:
                cipher += " "
        return cipher

    def decode(self, message):
        message += " "
        decipher = ""
        citext = ""
        for letter in message:
            if letter != " ":
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    decipher += " "
                else:
                    decipher += list(MORSE_CODE_DICT.keys())[
                        list(MORSE_CODE_DICT.values()).index(citext)
                    ]
                    citext = ""
        return decipher