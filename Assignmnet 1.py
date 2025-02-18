# assignment.py

def encrypt(message, key):
    """Encrypts the message by shifting ASCII values by the key."""
    encrypted_message = ""  # Initializing an empty string to hold the encrypted message
    key = key % 95  # Reduce the key to fit within the printable ASCII range (95 printable characters)
    for char in message:  # Iterate  or moving over each character in the input message
        # Shift the ASCII value of the character by the key
        shifted = ord(char) + key
        # Check if the shifted value exceeds the printable ASCII range
        if shifted > 126:  # 126 is the highest printable ASCII character
            # Wrap around to the beginning of the printable ASCII range
            shifted = 32 + (shifted - 127)
        # Convert the shifted ASCII value back to a character and append to the result
        encrypted_message += chr(shifted)
    return encrypted_message  # Returning the final encrypted message

def decrypt(encrypted_message, key):
    """Decrypts the message by shifting ASCII values backward by the key."""
    decrypted_message = ""  # Initializing an empty string to hold the decrypted message
    key = key % 95  # Reduce the key to fit within the printable ASCII range (95 printable characters)
    for char in encrypted_message:  # Iterate over each character in the encrypted message
        # Shift the ASCII value of the character backward by the key
        shifted = ord(char) - key
        # Check if the shifted value goes below the printable ASCII range
        if shifted < 32:  # 32 is the lowest printable ASCII character
            # Wrap around to the end of the printable ASCII range
            shifted = 127 - (32 - shifted)
        # Convert the shifted ASCII value back to a character and append to the result
        decrypted_message += chr(shifted)
    return decrypted_message  # Return the final decrypted message

def main():
    """Main function to handle user input and execute encryption or decryption."""
    try:
        # Asking  the user to enter a message
        message = input("Enter the message: ")
        
        # Asking  the user to enter a key and strip any extra whitespace
        key_input = input("Enter the key (an integer): ").strip()
        
        # Checking if the input is empty
        if not key_input:
            print("Error: Key cannot be empty. Please enter a valid integer.")
            return
        
        # Checking if the input is a valid integer
        if not key_input.lstrip('-').isdigit():  # Allow negative numbers
            print("Error: Please enter a valid integer for the key.")
            return
        
        # Convert the input key to an integer
        key = int(key_input)  # This should now succeed if the input is valid
        
        # Validate that the key is a non-negative integer
        if key < 0:
            print("Error: Key must be a non-negative integer.")
            return  # Exit the function if the key is invalid
        
        # Asking  the user to choose the mode of operation
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

        # Checkimg the selected mode and perform the corresponding action
        if mode == "encrypt":
            result = encrypt(message, key)  # Call the encrypt function
            print(f"Encrypted message: {result}")  # Display the encrypted message
        elif mode == "decrypt":
            # Asking the user  for confirmation before decrypting
            confirm = input("Are you sure you want to decrypt this message? (yes/no): ").strip().lower()
            if confirm == 'yes':
                result = decrypt(message, key)  # Calling the decrypt function
                print(f"Decrypted message: {result}")  # Displaying the decrypted message
            else:
                print("Decryption canceled.")  # Informing the user that decryption was canceled
        else:
            print("Error: Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")  # Handle invalid mode input
    
    except ValueError:
        # Handling the case where the key input is not a valid integer
        print("Error: Please enter a valid integer for the key.")

# This condition checks if the script is being run directly 
if __name__ == "__main__":
    main()  # Calling the main function to execute the program