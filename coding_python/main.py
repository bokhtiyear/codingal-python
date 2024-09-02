def setOrnot(number,n):
    if number & (1<<(n-1)):
        print("Set")
    else:
        print("Not set") 
        
        
number = int(input("Enter a number"))
n = int(input("Enter a bit number"))
setOrnot(number,n)   