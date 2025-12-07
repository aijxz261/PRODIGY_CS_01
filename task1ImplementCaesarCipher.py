def caesar(text, shift, encrypt=True):
    result = ""
    if not encrypt:          # for decrypt, just reverse the shift
        shift = -shift

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


# --- simple menu ---
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice (1/2): ")
message = input("Enter message: ")
shift = int(input("Enter shift (1-25): "))

if choice == "1":
    print("Encrypted:", caesar(message, shift, True))
else:
    print("Decrypted:", caesar(message, shift, False))
