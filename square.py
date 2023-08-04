def square_multiply(a,x,n):
    y=1
    #n_b is the number of bits in x
    n_b=bin(x)[2:]
    for i in n_b[::-1]:
        if i =='1':
            y=(y*a)%n
        a=(a*a)%n
    return y

e = 65537
d = 879218557499725217
p = 4994984933
q = 4881862009
n = p*q

message = 123456789

encrypt = square_multiply(message,e,n)
print(encrypt)
decrypt = square_multiply(encrypt,d,n)
print(decrypt)