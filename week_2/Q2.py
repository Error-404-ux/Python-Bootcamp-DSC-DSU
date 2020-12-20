import csv
l=[]
dict1={}
base__url="https://www.facebook.com/"
with open("Fb_page_handel.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {row}')
            line_count += 1
        else:
            l.append(row[0])
            line_count += 1
print(l)   
for name in l:
    response = requests.get(base__url+name)
    soup = BeautifulSoup(response.content,"html.parser")
    likes=soup.select_one("div._2pi9._2pi2 div._4bl9").text
    dict1[name]=[likes]
with open('Fb_Page_Likes.csv', 'w') as f:
    f.write('Fb_Handle,Likes\n')
    for key in dict1.keys():
        f.write("%s,%s\n"%(key,dict1[key]))
print("Done")