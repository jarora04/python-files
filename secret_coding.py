import string
import random
coding=input("enter the coding(1:True, 0:False): ")
st=input("enter the message:")
N = 3
res = ''.join(random.choices(string.ascii_lowercase +
							string.digits, k=N))

q=3
ptr=''.join(random.choices(string.ascii_lowercase +
							string.digits, k=q))

words=st.split(" ")

if(coding):
    nwords=[]
    for word in words:    
        if(len(word)>=3):
            new=str(res)+word[1:]+word[0]+str(ptr)
            nwords.append(new)
        else:
            nwords.append(word[::-1])
    
    print(" ".join(nwords))            
    
else:
    nwords=[]
    for word in words:    
        if(len(word)>=3):
            new=word[3:-3]
            new=new[-1]+new[0:-1]
            nwords.append(new)
        else:
            nwords.append(word[::-1])
    
    print(" ".join(nwords))
        