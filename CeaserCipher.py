
#Ceaser cipher
#pt=Tejas  ct=whmdv

def encryption(PT,key):
    
    CT=""
    
    alp='abcdefghijklmnopqrstuvwxyz'
    for a in PT:
        ind=alp.index(a)
        #print(ind)
        
        if (ind+key)>25:
            mind=(ind+key)%26
        else:
            mind=ind+key
        CT=CT+alp[mind]
    print("Enryption:\n Plain Text: "+PT+"Cipher Text: "+CT)

def decryption(CT,key):
    PT=""
    alp='abcdefghijklmnopqrstuvwxyz'
    for a in CT:
        ind=alp.index(a)
        #print(ind)
        
        if (ind+key)>25:
            mind=(ind-key)%26
        else:
            mind=ind-key
        PT=PT+alp[mind]
    print("Decryption:\nCipher Text: "+CT+" Plain Text: "+PT)
    
encryption("tejas",3)
decryption("whmdv",3)

