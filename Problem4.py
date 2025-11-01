# Label the program written in problem 4 with Comments

import os

#Specify the directory you want to list
directory_path = 'D:'

# Print each file and directory name
contents = os.listdir(directory_path)

# Print each file and directory Name
for item in contents:
    print(item)