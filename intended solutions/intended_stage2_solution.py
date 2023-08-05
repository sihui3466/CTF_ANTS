otp_key    = "01101011111010110" # from timing the intervals before each bit is printing
ciphertext = "11101011111010111" # from the output printed in stage 2
plaintext = bin(int(otp_key, 2) ^ int(ciphertext, 2))[2:]

print("The plaintext is:", plaintext)


