import time
import hashlib

# Function to hash the text using SHA-256
def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Stage 1: Read cipher text from file and prompt user to decipher
file_path = "WRITINGSONTHEWALL.txt"
with open(file_path, 'r') as file:
    cipher_text = file.read().strip()
    print("Cipher text:")
    print(cipher_text)
    print("\nPlease decipher the above text using a Caesar cipher on an external website.")

correct_deciphered_text_hash = "733efe065b321dd4862e9d1cc441c39046b01bf41bb24acedcec8614ade9ec7e"  # Replace with the hash of the correct deciphered text
user_deciphered_text = input("Enter the correct deciphered text: ")
while hash_text(user_deciphered_text) != correct_deciphered_text_hash:
    user_deciphered_text = input("Incorrect! Please try again or enter 'exit' to quit: ")
    if user_deciphered_text.lower() == 'exit':
        print("Exiting game. Goodbye!")
        exit()

print("Correct deciphered text! Proceeding to the next stage...")

# Stage 2a: Extract RSA public key n
print("\nStage 2a: Extract the RSA public key n from the deciphered text.")

# Stage 2b: Perform timing attack and request user to enter OTP key
def perform_timing_attack():
    plaintext = "10000000000000001"
    key = "01101011111010110"
    encrypted_text = ''.join(str(int(a) ^ int(b)) for a, b in zip(plaintext, key))
    print("OTP encrypted key:")
    for bit in range(len(plaintext)):
        if key[bit] == "0":
            time.sleep(0.5)
        else:
            time.sleep(1.5)
        print(encrypted_text[bit])
    return key

print("Stage 2b: Performing timing attack to find the OTP to decrypt the RSA exponent value.")
correct_key = perform_timing_attack()
user_key = input("Please enter the correct OTP key: ")
while user_key != correct_key:
    user_key = input("Incorrect OTP key! Please try again or enter 'exit' to quit: ")
    if user_key.lower() == 'exit':
        print("Exiting game. Goodbye!")
        exit()

print("Correct OTP key! Proceeding to the next stage...")

# Stage 3: Instructions for RSA decryption
print("\nStage 3: Use the simplified RSA decryption (square and multiply) to decrypt the password to a file.")
print("Note: Please refer to the specific instructions in the deciphered text for details on the RSA decryption process.")
