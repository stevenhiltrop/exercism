"""
Conversion functions for the NATO Phonetic Alphabet.
"""

# To save a lot of typing the code words are presented here
# as a dict, but feel free to change this if you'd like.
ALPHANUM_TO_NATO = {
    "A": "ALFA",
    "B": "BRAVO",
    "C": "CHARLIE",
    "D": "DELTA",
    "E": "ECHO",
    "F": "FOXTROT",
    "G": "GOLF",
    "H": "HOTEL",
    "I": "INDIA",
    "J": "JULIETT",
    "K": "KILO",
    "L": "LIMA",
    "M": "MIKE",
    "N": "NOVEMBER",
    "O": "OSCAR",
    "P": "PAPA",
    "Q": "QUEBEC",
    "R": "ROMEO",
    "S": "SIERRA",
    "T": "TANGO",
    "U": "UNIFORM",
    "V": "VICTOR",
    "W": "WHISKEY",
    "X": "XRAY",
    "Y": "YANKEE",
    "Z": "ZULU",
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "TREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINER",
}


def transmit(message: str) -> str:
    """
    Convert a message to a NATO code word transmission.

    :param
    message: str

    :return
    transmission: str
    """
    transmission = list()

    for letter in message:
        if letter.isascii() and letter.upper() in ALPHANUM_TO_NATO:
            transmission.append(ALPHANUM_TO_NATO[letter.upper()])

    return ' '.join(transmission)


def receive(transmission: str) -> str:
    """
    Convert a NATO code word transmission to a message.

    :param
    transmission: str

    :return
    message: str
    """
    message = str()

    def get_key_by_value(value):
        for item in ALPHANUM_TO_NATO.items():
            if item[1] == value:
                return item[0]

    for word in transmission.split():
        message += get_key_by_value(word)
    return message
