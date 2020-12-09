#Name = Laksh kumar
#Q1 reverse
b = input("Enter Your name: ") 
rows = len(b)
zero = "false"
for i in range(rows, -1, -1): #loop will start from length, if length of name is 6 then loop will start from 6 and then it will go -1 step until it reaches -1 index
    for j in range(i):
        if j == i-1:  
            print(b[i-1], end=' ')
        else:
            print(" ", end=' ')
    
    print(" ")