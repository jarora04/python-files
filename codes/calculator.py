
def add(a, b):
    return a + b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


def remainder(a,b):
    return a%b

def power(a,b):
    return a**b


a=int(input("entre the number: "))
b=int(input("enter the 2 number: "))
print(a,b)
select=int(input("enter the opperation(1:add, 2:subtract, 3:multiply, 4: divide, 5: remainder, 6: power): "))
 

if select == 1:
    print(add(a,b))
 
elif select == 2:
    print(subtract(a,b))
 
elif select == 3:
    print(multiply(a,b))
 
elif select == 4:
    print(divide(a,b))
    
elif select == 5:
    print(remainder(a,b))
    
elif select == 6:
    print(power(a,b))    
    
else:
    print("Invalid input")