#Vernam cipher
#PT=>Tejas
#key=>Happy

def encryption(PT,key):
    CT=""
    alp='abcdefghijklmnopqrstuvwxyz'
    i=0
    for a in PT:
        indPT=alp.index(a)
        indkey=alp.index(key[i])
        i=i+1
        indCT=indPT+indkey
        if indCT>=26:
            indCT =indCT%26
        CT=CT+alp[indCT]
    print("PT: "+PT+" Key: "+key+" CT: "+CT)    
        
encryption("tejas","happy")

def decryption(CT,key):
    PT=""
    alp='abcdefghijklmnopqrstuvwxyz'
    i=0
    for a in CT:
        indCT=alp.index(a)
        indkey=alp.index(key[i])
        i=i+1
        indPT=indCT-indkey
        if indPT>=26:
            indPT =indPT%26
        PT=PT+alp[indPT]
        
    print("CT: "+CT+" Key: "+key+" PT: "+PT)

decryption("aeypq","happy")
