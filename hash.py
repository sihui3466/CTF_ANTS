import hashlib

def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

correct_deciphered_text = "greatjobnewstageunlockedantsantsantsrsapublickeyn24384827179940110397publickeyantsantsantsnothingtoseeherelookelsewherenantsantsantsstartofaeskeytobedecodedbyrsaynxlzbpdvehefendantsantsants"
hashed_text = hash_text(correct_deciphered_text)

print("Hash of the correct deciphered text:")
print(hashed_text)
