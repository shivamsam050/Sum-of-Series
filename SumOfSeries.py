sum=0.0
n = int (input("Enter The Nth Number"))
print("Sum of Series=")
for i in range(4,n+1):
    for j in range(n+1):
        if(i== 2**j):
            sum = sum +1/float(i**2)
            print("1/(%d)^2 +" %(i )),
print("0")            
print("Sum Of the Above Series Is= ",sum)    