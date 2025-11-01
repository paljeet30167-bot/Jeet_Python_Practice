# Write a python program to print the contents of a directory using the os module.

import os

 
directory_path = 'D:'
 
contents = os.listdir(directory_path)
 
print(contents)
