# def fabonnci(a):
#     if(a==0):
#         return 0
#     elif(a==1):
#         return 1
#     else:
#         return fabonnci(a-1)+fabonnci(a-2)
    
  

# f=int(input("enter the value"))
# print(fabonnci(f))

def factorial(a):
    if(a==1 or a==0):
        return 1
    else:
        return a*factorial(a-1)
    
f=int(input("entre the value"))
print(factorial(f))    