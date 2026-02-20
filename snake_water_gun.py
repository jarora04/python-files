import random as r

def check(comp,user):
    if(comp==user):
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==1 and user==2):
        return -1
    if(comp==2 and user==0):
        return -1
    
    return 1
        
    
user=int(input("0 for snake, 1 for water and 2 for gun"))
comp=r.randint(0,2)
print(f"Computer choses {comp}")

score=check(comp,user)

if score==0:
    print("Its a draw")
elif score==1:
    print("you lose")
else:
    print("you win")


