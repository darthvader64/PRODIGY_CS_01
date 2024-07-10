def caesar_cipher(text, shift, mode):
    result = ""

    for i in range(len(text)):
        char = text[i]

#encryption and decryption for the word, checks upper and lowercase
        
        if char.isupper():
            if mode == "encrypt":
                result = result + chr((ord(char) + shift - 65) % 26 + 65)
            elif mode == "decrypt":
                result = result + chr((ord(char) - shift - 65) % 26 + 65)
     
        elif char.islower():
            if mode == "encrypt":
                result = result + chr((ord(char) + shift - 97) % 26 + 97)
            elif mode == "decrypt":
                result = result + chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result = result + char

    return result

#asking for user input
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift: "))

ciphertext = caesar_cipher(plaintext, shift, "encrypt")
decrypted_text = caesar_cipher(ciphertext, shift, "decrypt")

#displaying the results
print(f"Plaintext: {plaintext}")
print(f"Shift: {shift}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
