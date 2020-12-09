#Name = Laksh kumar
#Q2
length=5 #int(input("Enter Number of records you want to enter : "))
stud_records = {}
roll_list=[]
name_list=[]
age_list=[]
marks_list=[]
for i in range(length):
    roll_num = input("Enter Roll No. : ")
    roll_list.append(roll_num)
    
    name = input("Enter Name: ")
    name_list.append(name)
    
    age = input("Enter Age: ")
    age_list.append(age)
    
    marks = input("Enter Marks out of 100: ")
    marks_list.append(marks)
    print("\n")

    stud_records[roll_num] = [name,age,marks]

print("Roll_num",end="|\t")
print("Name",end="\t|\t")
print("Age",end="\t|\t")
print("Marks",end="\t|\t")
print("\n")
for i in range(length) :
    print(roll_list[i],end="\t|\t")
    print(name_list[i],end="\t|\t")
    print(age_list[i],end="\t|\t")
    print(marks_list[i],end="\t|\t")
    print("\n")
 