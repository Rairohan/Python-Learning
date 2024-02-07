c = input("enter any operator")
x = int(input("enter any number"))
y = int(input("enter any number"))
match c:
    case'+':
        print("the sum is",x+y)
    case'-':
        print("the sub is",x-y)
    case'*':
        print("the multiply is",x*y)
    case'/':
        print("the division is",x/y)
    case'_':
        print("enter the correct operator")


    

