from winsound import Beep
from time import sleep as delay


def encode(str_arg):
    morse_code = {
        "a": "-_", "b": "_---", "c": "_-_-", "d": "_--",
        "e": "-", "f": "--_-", "g": "__-", "h": "----",
        "i": "--", "j": "-___", "k": "_-_", "l": "-_--",
        "m": "__", "n": "_-", "o": "___", "p": "-__-",
        "q": "__-_", "r": "-_-", "s": "---", "t": "_",
        "u": "--_", "v": "---_", "w": "-__", "x": "_--_",
        "y": "_-__", "z": "__--", ".": "-_-_-_", ",": "__--__",
        "?": "--__--", "@": "-__-_-", "//": "_--_-", "1": "-____",
        "2": "--___", "3": "---__", "4": "----_", "5": "-----",
        "6": "_----", "7": "__---", "8": "___--", "9": "____-", "0": "_____"}

    def beeper(arg):
        if arg == "-":
            Beep(frequency=700, duration=200)
        elif(arg == "_"):
            Beep(frequency=700, duration=750)

    for letter in str_arg:
        if letter == " ":
            delay(1.2)
        else:
            if letter.isalpha():
                letter = letter.lower()
            x = morse_code[letter]
            for bits in x:
                beeper(bits)
        delay(1.8)


def main():
    info = """
        +----------+     +-------------+     +--------------+
        |  STRING  | --> |  ALGORITHM  | --> |  MORSE CODE  |
        +----------+     +-------------+     +--------------+

    The morse code encoding supports: all alphabets, all numbers, 
    and some special characters ( , . // @ ?)
    """
    print(info)
    code = input("Enter the string : ")

    encode(code)
    print("success!")

main()
