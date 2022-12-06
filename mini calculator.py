def add(a,b):
    return (a+b)
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return(a/b)
c=""
r=int(input())
while c=="":
    
    p=input()
    if p=="=":
        print(r)
        break
    elif p=="+":
        n=int(input())
        r=add(r,n)
    elif p=="-":
        n=int(input())
        r=sub(r,n)
    elif p=="*":
        n=int(input())
        r=mul(r,n)
    elif p=="/":
        n=int(input())
        r=div(r,n)
        
        
          
