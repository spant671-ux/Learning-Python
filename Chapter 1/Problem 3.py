import os

#Specify the directory you want to list
directory_path = "C:/New folder/Learning Python/Chapter 1"
 
#List all files in the specified directory
contents = os.listdir(directory_path)

#Print each file and directory name
for item in contents:
    print(item)
    
