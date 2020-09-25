import os

# ( print current direcory )
# path = os.getcwd()
# print("The current working directory is %s" % path)


path = "Users\oliva\Desktop\Images"

try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)
