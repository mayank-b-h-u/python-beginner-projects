while True:
 def invca(inv) :
    if inv==0 or inv>=5:
     print("Calculator band ho gaya")
     continue
 def add(a,b):
    return a + b
 def sub(a,b):
    return a - b
 def mul(a,b):
    return a * b
 def div(a,b):
    if b==0:
        print("zero is not devide by a ")
    else:
     return a / b
 print("_____Simple calculater_____")
 print("1. Add")
 print("2. Subtract")
 print("3. multiply")
 print("4 divide ")
 c=int(input())
 print(invca(c),"involed input ")
 print("enter the first number ")
 x=float(input())
 print("Enter the secod number ")
 y=float(input())
 match c:
    case 1:
        print(add(x,y))
    case 2:
        print(sub(x,y))
    case 3:
        print(mul(x,y))
    case 4:
        print(div(x,y))


