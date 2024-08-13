import re

# Creating a dictionary to store the morse code and its corresponding character
morse_code = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
              "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
              "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
              "-.--": "Y", "--..": "Z", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5",
              "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0", ".-.-.-": ".", "--..--": ",",
              "---...": "?", "..--..": "/", '.......': " ", ".-...": "'"}

# Creating a dictionary to store the character and its corresponding morse code
txt_code = {value: key for key, value in morse_code.items()}


# Function to convert a string to morse code
def string_to_morse(string):
    morse_code_string = ""
    for char in string:
        morse_code_string += txt_code[char] + " "
    return morse_code_string


# convert string to proper sentence
def string_to_sentence(string):
    strings = re.split(r'(?<=[.!?]) +', string)
    sentences = [string[0].upper() + string[1:].lower() for string in strings]
    return ' '.join(sentences)


# Function to convert morse code to string
def morse_to_string(morse_code_string):
    string = ""
    morses = morse_code_string.split(" ")
    for morse in morses:
        try:
            if morse in morse_code.keys():
                string += morse_code[morse]
            else:
                raise KeyError
        except KeyError:
            print("Invalid morse code")
            exit()

    return string_to_sentence(string)


def try_again():
    choice = input("Do you want to try again? (y/n): ")
    if choice.lower() == "y":
        morse_on = True
    else:
        morse_on = False
        print("Thank you for using the Morse Code Converter!")
    return morse_on


morse_on = True
while morse_on:
    # Main program
    print("Morse Code Converter")
    choice = input("Enter 1 to convert string to morse code or 2 to convert morse code to string: ")
    # Check if the user has entered a valid choice

    if choice == "1":
        input_string = input("Enter a string: ").upper()
        morse_code_string = string_to_morse(input_string)
        print(f"The morse code is:\n{morse_code_string}")
        morse_on = try_again()
    elif choice == "2":
        morse_code_string = input("Enter morse code: ").upper()
        input_string = morse_to_string(morse_code_string)
        print(f"The secret message is:\n{input_string}")
        morse_on = try_again()
    else:
        print("Invalid choice")
        morse_on = try_again()
