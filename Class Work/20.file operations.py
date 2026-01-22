# File Operations in Python
# This script demonstrates basic file operations such as creating, writing, reading, and appending to a file.
# Creating and writing to a file

# 1.Creating and writing to a file :

try:
    file=open('batch.txt','r')
except Exception as e:
    print(f"error occured:{e}")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()
    
# 2. with open('batch.txt','w') as file:

with open('batch.txt', 'w') as file:
    print(file.read())

# 3. Appending to a file :

import os 
os.mkdir('batch-43')
os.rmdir('batch-43')

# 4.

import os   