
def playfair_cipher(key,message):
    key=''.join(dict.fromkeys(key.upper()+"ABCDEFGHIKLMNOPQRSTUVWXYZ".replace('J','')))
    table=[key[i:i+5] for i in range(0,25,5)]
    
    message=message.replace('J','I').upper()
    
    pairs=[]
    i=0
    while i<len(message):
        a=message[i]
        b=message[i+1] if i+1<len(message) else 'X'
        if a==b:
            pairs.append((a,'X'))
            i+=1
        else:
            pairs.append((a,b))
            i+=2
    
    def encrypt(pair):
        idx1,idx2=key.index(pair[0]),key.index(pair[1])
        row1,col1=divmod(idx1,5)
        row2,col2=divmod(idx2,5)
        if(row1==row2):
            return table[row1][(col1+1)%5]+table[row2][(col2+1)%5]
        elif col1==col2:
            return table[(row1+1)%5][col1]+table[(row2+1)%5][col2]
        else:
            return table[row1][col2]+table[row2][col1]
    
    encrypted_message=''.join(encrypt(pair) for pair in pairs)
    return encrypted_message

key=input("enter the key")
message=input("enter the message")
print(playfair_cipher(key,message))
