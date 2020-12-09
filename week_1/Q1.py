#Name = Laksh kumar
#Q1
name=input("Enter Your Name : ")
rows=len(name)
for x in range(rows+1):
  for y in range(x):
    if y == x-1:
        print(name[x-1],end=" ")
    else:
        print(" ",end=" ")
    
  print(" ")    