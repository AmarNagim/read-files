import time
with open('/Users/amarnagim/Library/CloudStorage/OneDrive-DaVinciCollege/Da Vinci College/software_developen/Assignments/jaar_1/periode_1/fase_1/09_data:files:state.save/read-files/README.md', 'r') as myFile:
    line = True
    while line:
        line = myFile.readline()
        print(line)
        time.sleep(1)


