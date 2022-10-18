#Transposition technique
#Rail fence

#PT-tejas
#t j s
# e a
#CT-tjsea

fv=[]
sv=[]

def encrypt(msg):
    strg=" "
    for v in range(0,len(msg)):
        if(v%2==0):
            fv.append(msg[v])
        else:
            sv.append(msg[v])
    print(strg)
    for v in fv:
        strg=strg+v
    for v in sv:
        strg=strg+v
    print("Encrypted message: ",strg)

def decrypt(msg):
    strg=""
    le=len(msg)//2
    #if message length is odd we are adding 1 to len(msg)//2
    if(len(msg)%2!=0):
        le=le+1
        print(le)
    print("len/2=",le)
    #diving the message by m
    m=le
    
    for i in range(0,le):
        if(m<len(msg)):
            strg=strg+msg[i]+msg[m]      
        m=m+1   
        #print("after addm",i,m,strg)
    if len(msg)%2!=0:
        strg=strg+msg[i]
    print("Decrypted message: ",strg)
    
encrypt("tejas")
decrypt("tjsea")
