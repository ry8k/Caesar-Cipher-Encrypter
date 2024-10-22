import art

# Caeser ciper encrypter

# Set a variable to keep the while loop running
keeprunning = True

# List of letters in the alphabet, repeated twice to allow for wrapping
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Print out the logo
print(art.logo)

# Loop until the user chooses to quit
while keeprunning == True: 
    
    # Ask the user if they want to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    
    # Ask for the message to be encrypted or decrypted
    text = input("Type your message:\n").lower()
    
    # Ask for the shift value
    try:  
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("That's not a valid number!")
        continue

    def caeser(plain_text, shift_amount, direction):
        """
        This function takes in three parameters:

        - plain_text: The string that needs to be encrypted or decrypted.
        - shift_amount: The number of positions each letter in the plain_text should be shifted.
        - direction: A string indicating whether to encrypt or decrypt the plain_text. Must be either "encode" or "decode".

        The function returns nothing, but prints out the encrypted or decrypted text.
        """
        if direction == "encode":
            """
            When direction is "encode", the function will encrypt the plain_text by shifting each letter by the shift_amount.
            The shift_amount is taken modulo 26 so that the shift wraps around the alphabet if it exceeds 26.
            """
            shift_amount = shift_amount % 26
            cipher_text = ""
            for letter in plain_text:
                """
                Iterate through each letter in the plain_text.
                If the letter is not in the alphabet, just append it to cipher_text as is.
                If the letter is in the alphabet, find its index in the alphabet, add the shift_amount to it, and use the new index to get the encrypted letter from the alphabet.
                Append the encrypted letter to cipher_text.
                """
                if letter not in alphabet:
                    cipher_text += letter
                else:
                    position = alphabet.index(letter)
                    new_position = position + shift_amount
                    cipher_text += alphabet[new_position]
            print(f"The encoded text is {cipher_text}")
                
        elif direction == "decode":
            """
            When direction is "decode", the function will decrypt the plain_text by shifting each letter by the negative shift_amount.
            The shift_amount is taken modulo 26 so that the shift wraps around the alphabet if it exceeds 26.
            """
            shift_amount = shift_amount % 26 
            cipher_text = ""
            for letter in plain_text:
                """
                Iterate through each letter in the plain_text.
                If the letter is not in the alphabet, just append it to cipher_text as is.
                If the letter is in the alphabet, find its index in the alphabet, subtract the shift_amount from it, and use the new index to get the decrypted letter from the alphabet.
                Append the decrypted letter to cipher_text.
                """
                if letter not in alphabet: 
                    cipher_text += letter   
                else:
                    position = alphabet.index(letter)
                    new_position = position - shift_amount
                    cipher_text += alphabet[new_position]
            print(f"The decoded text is {cipher_text}")
        else:
            print("Please enter a valid option.")

    # Call the caeser function to encrypt or decrypt the text
    caeser(text, shift, direction)

    # Ask the user if they want to go again
    z = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").strip().lower()

    # If the user types 'yes', set keeprunning to True
    # If the user types 'no', set keeprunning to False
    # If the user types anything else, set keeprunning to True (default to yes)
    if z == 'yes':
        keeprunning = True
    elif z == 'no':
        keeprunning = False
    else:
        keeprunning = True

