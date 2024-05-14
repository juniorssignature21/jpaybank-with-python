import os

file_name = 'data.txt'

with open(file_name, 'r') as f:
    file = f.read()
    print(file)    
    # for row in file:
    #     print(row)

file_name2 = 'none.txt'

with open(file_name2, 'w') as w:
    data = 'writing into file that does not exist\n'
    w.write(data)

with os.scandir('C:/Users') as entries:
    for entry in entries:
        print(entry.name)


with open(file_name2, 'a') as a:
    text_content = 'Welcome to Learn factory'
    a.write(text_content)

if os.path.exists(file_name2):
    os.remove(file_name2)
else:
    print("Path does not exist")