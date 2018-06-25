import binascii


def to_encrypt(text, delta):
    ciphertext = ''
    for word in text:
        if word == ' ':
            encrypt_word = ' '
        else:
            word_ascii = ord(word)
            if word_ascii + delta > ord('z'):
                tmp = word_ascii + delta - ord('z') - 1
                k = ord('a') + tmp
                encrypt_word = chr(k)
            elif word_ascii + delta < ord('a'):
                tmp = ord('a') - word_ascii - delta - 1
                k = ord('z') - tmp
                encrypt_word = chr(k)
            else:
                encrypt_word = chr(word_ascii + delta)
        ciphertext = ciphertext + encrypt_word
    return ciphertext


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
