import random
s = input("Enter a string : ")
result = ''.join(format(ord(i),'08b') for i in s)  #This line converts each character of the string into 8 bits binary
answer=""
for i in range(len(result)):
    if(i%8 != 0):            #here the first bit of every character is not considered as it just indicates the sign of the character
        answer+=result[i]      #the rest of the bits (apart from first bits) is appended to answer vriable

# division of the answer bits into halves (Left and Right)
l = int(len(answer)/2)
left = answer[:l]
right = answer[l:]

lt = [2,3,6,7,1,6,5,9]  # shift box
keys=[]

for i in range(0,8):
    newKey = ""
    newAnswer = ""
    
    nl=int(left,2)         #conversion of binary left part to int
    nl=bin(nl<<lt[i])      #shifting the entire left integer
    num=2+lt[i]
    
    nr = int(right,2)
    nr = bin(nr<<lt[i])
    num=2+lt[i]
    
    newKey = nr[num:]+nl[num:]
    rm =[]
    
    while(len(rm) != 8):
        r = random.randint(0,len(newKey)-1)
        if(r not in rm):
            rm.append(r)
        for i in range(len(newKey)):
            if(i not in rm):
                newAnswer+=newKey[i]
        keys.append(newAnswer)
for i in range(0,len(keys)):
        print("Key ",i+1," = ",keys[i])