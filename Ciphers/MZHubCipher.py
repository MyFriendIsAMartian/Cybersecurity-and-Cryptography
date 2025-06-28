### This is something that I got from a book once! ###

opposites = {
    "A" : "G",      "a" : "g",
    "B" : "H",      "b" : "h",
    "C" : "I",      "c" : "i",
    "D" : "J",      "d" : "j",
    "E" : "K",      "e" : "k",
    "F" : "L",      "f" : "l",
    "G" : "A",      "g" : "a",
    "H" : "B",      "h" : "b",
    "I" : "C",      "i" : "c",
    "J" : "D",      "j" : "d",
    "K" : "E",      "k" : "e",
    "L" : "F",      "l" : "f",
    "M" : "Z",      "m" : "z",
    "N" : "T",      "n" : "t",
    "O" : "U",      "o" : "u",
    "P" : "V",      "p" : "v",
    "Q" : "W",      "q" : "w",
    "R" : "X",      "r" : "x",
    "S" : "Y",      "s" : "y",
    "T" : "N",      "t" : "n",
    "U" : "O",      "u" : "o",
    "V" : "P",      "v" : "p",
    "W" : "Q",      "w" : "q",
    "X" : "R",      "x" : "r",
    "Y" : "S",      "y" : "s",
    "Z" : "M",      "z" : "m"
}


print("\nThis cipher swaps the letters in a three circle pattern. A-L, N-Y, and M/Z sre the circles.")
print("As a symmetrical cipher, just enter the ciphertext back into the same program to retrieve the plaintext.")

message = input("\nPlease enter your message here, which will then be encrypted using this cipher: ")

message = message.translate(str.maketrans(opposites))

print("\n" + message)
