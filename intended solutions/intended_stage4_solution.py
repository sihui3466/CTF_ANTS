import time

def square_multiply(a,x,n):
    y=1
    n_b=bin(x)[2:]
    for i in n_b[::-1]:
        if i =='1':
            y=(y*a)%n
        a=(a*a)%n
    return y

start=time.time()

ciphertext = 10296304397633056706 # from stage 1
n = 24384827179940110397 # from stage 1
d = 879218557499725217 # from stage 3

decrypt = square_multiply(ciphertext,d,n)
print("password for file:", decrypt)

end=time.time()
diff=end-start
print("Time taken:",diff,"s")
