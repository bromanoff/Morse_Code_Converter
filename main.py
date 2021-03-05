import alphabet
from asci_headline import headline

print(headline)

def split(message):
	return [char.capitalize() for char in message] 

def convert():
    message = ""
    query = input("\nPlease enter the message you want to to translate: ")
    # Quit option
    if query == "quit":
        if input("Are you sure? (y/n): ") == "y":
            raise SystemExit("Exit program\n")
    
    for cipher in split(query):
        if cipher in alphabet.alphabet:
            message += alphabet.alphabet[cipher]
        else:
            message += "/    "
    print(f"Your morse code: {message} \nType 'quit' to exit")

while True:
    convert()