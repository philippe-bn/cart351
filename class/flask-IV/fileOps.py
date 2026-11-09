rainbowFile = open("files/rainbow.txt", "r")

# sampleFile = open("files/sample_text_rev.txt", "w")
# for i in range(3): 
#     a_name = input("Enter the name of the animal: ") 
#     sampleFile.write(a_name) 
#     sampleFile.write("\n") 
# sampleFile.close() 
# print("Data is written into the file.") 

# colorList = [] 
# for i in range(3): 
#     a_name = input("Enter the name of a color: ") 
#     colorList.append(a_name + '\n') 
# sampleFile.writelines(colorList) 
# sampleFile.close() 
# print("Data is written into the file.") 

# sampleFile_a = open("files/sample_text.txt", "a")
# nameList = [] 
# for i in range(3): 
#     a_name = input("Enter the name of someone in your class: ") 
#     nameList.append(a_name + '\n') 
# sampleFile_a.writelines(nameList) 
# sampleFile_a.close() 
# print("Data is written into the file.") 

# Read from file and parse JSON
import json
# jsonFile = open("files/test.json", "r")
# data = json.load(jsonFile)
# print(data)
# print(type(data)) # a list

# json_str = '{"name":"Sabs", "fav_col":"red", "fav_city":"montreal"}'
# data_2 = json.loads(json_str) 
# print(data_2)
# print(type(data_2))#converts to a dict

# jsonFile = open("files/test.json", "r")
# out_all_as_string = jsonFile.read()
# data_3 = json.loads(out_all_as_string) 
# print(data_3)
# print(type(data_3[0]))

# data_toSave = {"name":"mandy", "fav_col":"blue", "fav_city":"winnipeg"}
# #convert dictionary to str
# jsonStr = json.dumps(data_toSave, indent=4)
# #open or create if non existent
# fileOpen = open("files/new_sample.json","w")
# fileOpen.write(jsonStr)

# jsonFile = open("files/new_sample_b.json", "w")
# data_toSave_2= {"name":"mandy", "fav_col":"blue", "fav_city":["list",3,4,True,"abc"]}
# json.dump(data_toSave_2,jsonFile, indent =4)

jsonFile = open("files/new_sample_b.json", "r+")
data = json.load(jsonFile)
print(data['fav_city'])
print(type(data['fav_city']))
# #go to beginning of file
jsonFile.seek(0)
data['fav_city'].append("another element")
data["newKey"] = 1234
#output to the file
json.dump(data,jsonFile, indent =4)