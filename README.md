# CTF_ANTS

Background:

All teams will have to play as different ant colonies on a mission to retrieve treasured treats from the top tier of the cake plate as tasked by the queen ant. Each step of the journey up the cake plate is part of the challenge, once the contents of the file of the top tier (stage 3) has been revealed, the ant colonies will reach their goal of retrieving the treats for their queen.

Stage 1A: The queen loves swapping around alphabets and numbers → alphanumeric caesar’s cipher

The bottom tier cake plate (stage 1) has a wheel with 36 sections around it that spins freely, worker ants have to work together to spin the wheel to the correct location so that they can proceed to the next tier. The ants however, do not know how to position the wheel in the correct position. So they looked around for clues and they found some writing on the walls, writingsonthewall.txt. The ants use the text found to find the correct value of n to shift the wheel to the appropriate position. Ants will then find out the plaintext which contains english words which will signify the value of public key n and ciphertext needed for future stages.

Stage 1B:
To find the integer ‘e’ for the RSA public key, the ants have to apply what they have learned in Week 9 (time based side-channel attack). 
