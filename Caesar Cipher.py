def caesar_cipher(str,n):
    w=""
    for i in str:
        if(i.isalpha()):
            if(i.isupper()):
                w+=chr((ord(i)+n-65)%26+65)
            else:
                w+=chr((ord(i)+n-97)%26+97)
        else:
            w+=i
    return w
s=input("Enter the string to be encrypted : ")
shift=int(input("Enter the key value:"))
print(caesar_cipher(s,shift))