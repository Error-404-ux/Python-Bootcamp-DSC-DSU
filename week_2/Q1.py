import os
path1=input("Enter Path : ")
if path1=='':
    print("No path found in input printing current path data: ")
    path1="G:\\Python Bootcamp\\Python-Bootcamp-DSC-DSU\\week_2"
def main(path="G:\Python Bootcamp\Python-Bootcamp-DSC-DSU\week_2"):
    dict={}
    dict1={}
    data=os.listdir(path)
    os.chdir(path)
    for datas in data:
        statinfo = os.stat(datas)
        dict[datas] = [statinfo[6]]
        dict1[statinfo[6]] = [datas]
    for key, value in sorted(dict.items(), key=lambda item: item[1]): # lambda is a one line function. item is its parameter and item[1] means sort by value in dictionary     
        print("%s: %s" % (key, value))
                                                                    


if __name__ == '__main__':
	main(path1)  
