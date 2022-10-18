def encryption(PT):
    CT=""
    apl1='abcdefghijklmnopqrstuvwxyz'
    apl2='zyxwvutsrqponmlkjihgfedcba'
    for a in PT:
        ind=apl1.index(a)
        CT=CT+apl2[ind]
    print("Enryption:\ Plain text: "+PT+" Cipher text: "+CT)

encryption("tejas")

def decryption(CT):
    PT=""
    
    apl1='zyxwvutsrqponmlkjihgfedcba'
    apl2='abcdefghijklmnopqrstuvwxyz'
    for a in CT:
        ind=apl1.index(a)
        PT=PT+apl2[ind]
    print("Decryption:\ Cipher text: "+CT+" Plain text: "+PT)
decryption("gvqzh")
