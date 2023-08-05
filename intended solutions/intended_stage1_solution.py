def caesar_cipher(input_string, shift):
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return input_string.translate(table)

input_string = "al84ndi5h8qmn4a8ohfi6e874hnm4hnm4hnmlm4jo5fc6e8shwyx2y2w1v133yuvvux31jo5fc6e8s4hnm4hnm4hnmmn4lni9j4mmqil7ni58786i7875slm4vuw30xuyx310xxuz01u08h7"
shift = 6
print("The ciphered string is:", caesar_cipher(input_string, shift))
