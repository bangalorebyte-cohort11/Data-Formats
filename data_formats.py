
import csv

#reading csv files and printing in different formats
with open('movie_metadata.csv',"r") as g:
    g_csv = csv.reader(g)
    for i in g_csv:
        print(i)

# writing csv files

header = ["Name","Age","Height"]
student_names = ["Khulood","Madhan","Mathai"]
student_ages = [25,25,25]

with open('byte_students.csv','w') as csv_file:
	writer = csv.writer(csv_file,delimiter=',')
	writer.writerow(header)
	for i in student_names:
		writer.writerow([i])			

#JSON
# writing to json
import json
info = {
'name' : 'Uday',
'Age' : 26
}
print(type(info))

json_sr = json.dumps(info)
print(json_sr)
print(type(json_sr))

#reading from json
info = json.loads(json_sr)
#print(type(info))
#print(info)

#if working with files instead of string, use .dump and .load

# encoding and decoding 

byte  = b'This is a byte object'
print(byte)
print(type(byte))

also_byte = '字'
#print(also_byte)

list_= ["uday","uday"]
string_to_byte = bytes(list_[0],'utf-8')
print(string_to_byte)
print(type(string_to_byte))
byte_to_string = string_to_byte.decode()
print(byte_to_string)
print(type(byte))
"""


