import time 

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
