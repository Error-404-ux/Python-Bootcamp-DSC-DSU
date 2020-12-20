import requests
import json
import csv
dict1={}
url="https://directory.ntschools.net/api/System/GetAllSchools"
response = requests.get(url)
parsed_data = json.loads(response.content)
link="https://directory.ntschools.net/api/System/GetSchool?itSchoolCode="
school_codes = []
for code in parsed_data:
    school_codes.append(code['itSchoolCode'])
counter=0
for code in school_codes:
    if counter==50:
        break
    counter+=1
   # print("==========={}===========\n".format(counter))
    try:
        school_data = requests.get(link+code)
        school_data1 = json.loads(school_data.content)
       # print(school_data1['name'])
        #print(school_data1['physicalAddress']['description']+", "+test['physicalAddress']['state']+", "+test['physicalAddress']['postCode']+", "+test['physicalAddress']['displayAddress'] )
        address =school_data1['physicalAddress']['description']+", "+test['physicalAddress']['state']+", "+test['physicalAddress']['postCode']+", "+test['physicalAddress']['displayAddress']  
       # print(school_data1['schoolManagement'][0]['firstName'] +" "+ test['schoolManagement'][0]['lastName'])
        name=school_data1['schoolManagement'][0]['firstName'] +" "+ test['schoolManagement'][0]['lastName']
       # print(school_data1['schoolManagement'][0]['position'])
        position=school_data1['schoolManagement'][0]['position']
       # print(school_data1['schoolManagement'][0]['email'])
        email=school_data1['schoolManagement'][0]['email']
       # print(school_data1['schoolManagement'][0]['phone'])
        phone=school_data1['schoolManagement'][0]['phone']
        dict1[school_data1['name']] = [address,name,position,email,phone]
        #print("\n")
    except TypeError:
        continue
with open('Schools_Data.csv', 'w') as f:
    f.write('SchoolName,Address,description,state,postCode,displayAddress,name,position,email,phone\n')
    for key in dict1.keys():
        f.write("%s,%s\n"%(key,dict1[key]))
print("Done")