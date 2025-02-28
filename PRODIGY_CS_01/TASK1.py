def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - offset) % 26 + offset)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift - offset) % 26 + offset)
        else:
            decrypted_text += char
    return decrypted_text


def main():
    print("Caesar Cipher Encryption and Decryption")

    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()

    if choice == 'e':
        message = input("Enter your message to encrypt: ")
        shift = int(input("Enter the shift value (integer): "))
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")

    elif choice == 'd':
        encrypted_message = input("Enter the encrypted message to decrypt: ")
        shift = int(input("Enter the shift value (integer): "))
        decrypted_message = caesar_decrypt(encrypted_message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")


if __name__ == "__main__":
    main()
