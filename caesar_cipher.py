

def encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        print("Encrypted message:", encrypt(text, shift))
    elif choice == 'D':
        print("Decrypted message:", decrypt(text, shift))
    else:
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")


if __name__ == "__main__":
    main()
